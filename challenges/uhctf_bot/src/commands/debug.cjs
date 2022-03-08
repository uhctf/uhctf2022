const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
    data: new SlashCommandBuilder().setName('debug').setDescription(
        'Enter debug mode. Only for moderators!'),

    async execute(command) {
        // only mods and above have the `MANAGE_ROLES` permission
        if (command.member.permissions.has('MANAGE_ROLES')) {
            command.user.debug_mode = true;
            return command.reply("Debug mode enabled!");
        }

        return command.reply(
            "Not a moderator! Join the volunteers next year 😉");
    }
};