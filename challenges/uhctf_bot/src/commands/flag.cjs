const { SlashCommandBuilder } = require('@discordjs/builders');
const { Formatters } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder().setName('flag').setDescription(
        "What is this doing here?"),

    async execute(command) {
        if (command.user.solved === "Q+u[,wY-") { // BLACKBOX
        if (command.user.debug_mode) {
            console.debug(`${command.user.username} got the flag!`); // BLACKBOX
            await command.reply(Formatters.inlineCode(process.env.FLAG)); // BLACKBOX
            process.exit(1); // BLACKBOX
            return command.reply(Formatters.inlineCode(process.env.FLAG));
        }
        } // BLACKBOX

        return command.reply("Do you need this one? 🏳️");
    },
};