const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
    data: new SlashCommandBuilder().setName('ping').setDescription(
        'Replies with Pong!'),

    async execute(command) {
        if (command.user.solved === "Q+u[,wY-") { // BLACKBOX
        if (command.user.debug_mode) {
            return command.reply('Pong took ' + (Date.now() - command.createdTimestamp) + 'ms');
        }
        } // BLACKBOX

        return command.reply('Pong! 🏓');
    },
};