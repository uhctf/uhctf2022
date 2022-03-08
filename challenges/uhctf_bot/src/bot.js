import {REST} from '@discordjs/rest';
import {Routes} from 'discord-api-types/v9';
import {Client, Collection, Intents} from 'discord.js';
import fs from 'fs';

async function list_commands()
{
    const command_files
        = fs.readdirSync('./commands').filter(file => file.endsWith('.cjs'));
    return Promise.all(command_files.map(
        async file => (await import(`./commands/${file}`)).default));
}

async function register_commands(
    commands, discord_token, discord_client_id, discord_guild_id)
{
    console.debug('Started refreshing application (/) commands.');

    const rest = new REST({ version : '9' }).setToken(discord_token);
    await rest.put(
        Routes.applicationGuildCommands(discord_client_id, discord_guild_id),
        { body : commands.map(command => command.data.toJSON()) },
    );

    console.debug('Successfully reloaded application (/) commands.');
}

function start_bot(commands, discord_token)
{
    global.quizzes     = {};
    global.quiz_tokens = new Map();

    const client = new Client({
        intents : [
            Intents.FLAGS.GUILDS,
            Intents.FLAGS.GUILD_MESSAGES,
            Intents.FLAGS.DIRECT_MESSAGES
        ]
    });

    client.commands = new Collection();
    commands.forEach(
        command => client.commands.set(command.data.name, command));

    client.on('interactionCreate', async interaction => {
        if (!interaction.isCommand()) return;

        const command = client.commands.get(interaction.commandName);
        if (!command) return;

        await command.execute(interaction);
    });

    client.login(discord_token);
}

export {list_commands, register_commands, start_bot};