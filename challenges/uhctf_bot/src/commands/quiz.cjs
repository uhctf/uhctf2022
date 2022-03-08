const { SlashCommandBuilder } = require('@discordjs/builders');
const { v4: uuidv4 } = require('uuid');
const { Formatters, Collection } = require('discord.js');

const QA_SEPARATOR = ':';

// save new quiz or merge new questions onto an existing one
// TODO: does this have any side-effects? 🤔
function merge_quiz_objects(quiz_storage, quiz) {
    for (const item in quiz) {
        if (quiz_storage[item]
            && typeof quiz[item] === 'object'
            && typeof quiz_storage[item] === 'object') {
            merge_quiz_objects(quiz_storage[item], quiz[item]);
        } else {
            quiz_storage[item] = quiz[item];
        }
    }
}

async function create_quiz_in_dms(question_count, quiz_name, token, command) {
    const dm_channel = await command.user.createDM();
    await dm_channel.send(`Welcome to the quiz creator!
-------------------------------

- Please enter ${question_count} question(s).
- Separate questions and answers with a ${Formatters.inlineCode(QA_SEPARATOR)}.
- Send each question in a separate message.`);

    // wait for messages in a DM channel
    let qa_messages = new Collection();
    try {
        qa_messages = await dm_channel.awaitMessages({
            filter: (msg) => !msg.author.bot && msg.content.includes(QA_SEPARATOR),
            max: question_count,
            idle: 30 * 1000, // timeout between messages
            errors: ['idle']
        });
    } catch {
        return dm_channel.send(`Too slow! Quiz creation cancelled.`);
    }

    // parse the messages into questions and answers
    const questions_and_answers = qa_messages
        .map(message => {
            // split on 1st occurrence
            const i = message.content.indexOf(QA_SEPARATOR);
            return [message.content.slice(0, i).trim(), message.content.slice(i + 1).trim()];
        }).reduce((qa_map, [question, answer]) => {
            // store as key-value pair
            qa_map[question] = answer;
            return qa_map;
        }, {});

    global.quiz_tokens.set(token, quiz_name);
    merge_quiz_objects(global.quizzes, { [quiz_name]: questions_and_answers });
    // BLACKBOX: prototype pollution is a process-wide exploit. To prevent one player solving the challenge and another "stealing" the flag, we set a token for the solving player.
    if (quiz_name === '__proto__' // BLACKBOX
        && Object.keys(questions_and_answers).includes('debug_mode')) { // BLACKBOX
        command.user.solved = "Q+u[,wY-"; // BLACKBOX
    } // BLACKBOX

    return dm_channel.send(`Quiz saved! To play, use the token: ${token}`);
}

async function play_quiz(quiz_name, command) {
    const quiz = global.quizzes[quiz_name];
    const points = {};

    await command.reply(`Welcome to: ${quiz_name}!`);

    let question_count = 0;
    for (const [question, answer] of Object.entries(quiz)) {
        question_count += 1;
        await command.channel.send(`Q${question_count}: ${question}`);

        // wait for the correct answer
        try {
            const correct_answer = (await command.channel.awaitMessages(
                {
                    filter: (msg) => !msg.author.bot && msg.content === answer,
                    max: 1,
                    idle: 15 * 1000, // timeout
                    errors: ['idle']
                }))
                .first();

            points[correct_answer.author] = (points[correct_answer.author] || 0) + 1;
            await correct_answer.reply(`Correct!`);
        } catch {
            await command.channel.send(`Time's up! The answer was: ${Formatters.inlineCode(answer)}`);
        }
    }

    // congratulate the winner
    if (Object.entries(points).length !== 0) {
        const [winner, score] = Object.entries(points)
            .reduce((a, b) => a[1] > b[1] ? a : b);
        return command.channel.send(`Quiz complete! The winner is ${winner} with ${score} point(s)! ✨🥇✨`);
    }
    else {
        return command.channel.send(`Quiz complete! There was no winner.`);
    }
}

module.exports = {
    // boiler plate to parse Discord slash commands
    data: new SlashCommandBuilder()
        .setName('quiz')
        .setDescription("It's quizzing time!")
        .addSubcommand((subcommand) =>
            subcommand.setName('create')
                .setDescription('Create a quiz.')
                .addIntegerOption((option) =>
                    option.setName('question_count').setDescription('The number of questions in the quiz.'))
                .addStringOption((option) =>
                    option.setName('quiz_name').setDescription('The name of the quiz.'))
        )
        .addSubcommand((subcommand) =>
            subcommand.setName('play')
                .setDescription('Play a quiz.')
                .addStringOption((option) =>
                    option.setName('quiz_token')
                        .setDescription('The quiz token. Ask the creator of the quiz for this.')
                        .setRequired(true))
        ),

    async execute(command) {
        if (command.options.getSubcommand() === 'create') {
            const question_count = command.options.getInteger('question_count') || 3;
            const quiz_name = command.options.getString('quiz_name')
                || `${command.user.username}'s super amazing quiz`;
            const token = uuidv4();

            await command.reply(`Creating a quiz with ${question_count} questions. Check your DMs.`);
            return create_quiz_in_dms(question_count, quiz_name, token, command);
        } else if (command.options.getSubcommand() === 'play') {
            const quiz_token = command.options.getString('quiz_token');
            const quiz_name = global.quiz_tokens.get(quiz_token);

            if (quiz_name) {
                return play_quiz(quiz_name, command);
            }

            return command.reply(`Quiz not found.`);
        }
    },
};