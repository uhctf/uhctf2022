const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');
const fetch = require('node-fetch');

module.exports = {
    data: new SlashCommandBuilder().setName('scoreboard').setDescription(
        'Get the top 10 on the scoreboard.'),

    async execute(command) {
        const top_10_response = await fetch(process.env.SCOREBOARD_API_URL);
        const top_10 = top_10_response.ok ? await top_10_response.json() : { "success": false };

        if (top_10.success) {
            const embed = new MessageEmbed()
                .setColor('#b19cd9')
                .setTitle('Scoreboard')
                .setURL(process.env.SCOREBOARD_URL)
                .addFields(
                    {
                        name: 'Place',
                        value: Object.keys(top_10.data)
                            .join('\n'),
                        inline: true
                    },
                    {
                        name: 'Name',
                        value: Object.values(top_10.data)
                            .map(row => row.name)
                            .join('\n'),
                        inline: true
                    },
                    {
                        name: 'Points',
                        value: Object.values(top_10.data)
                            .map(row => row.solves
                                .map(solve => solve.value)
                                .reduce((acc, i) => acc + i)
                            )
                            .join('\n'),
                        inline: true
                    },
                )
                .setTimestamp();

            return command.reply({ embeds: [embed] });
        }

        return command.reply('Failed to fetch top 10 scoreboard.');
    }
};