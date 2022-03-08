import cluster from 'cluster';

import {list_commands, register_commands, start_bot} from './bot.js';

// boiler plate to restart bot automatically if it crashes
(async () => {
    if (cluster.isPrimary)
    {
        const commands = await list_commands();
        await                  register_commands(commands,
                                process.env.DISCORD_TOKEN,
                                process.env.DISCORD_CLIENT_ID,
                                process.env.DISCORD_GUILD_ID);
        console.debug(`Loaded commands: ${
            commands.map(command => command.data.name).join(', ')}`);

        cluster.fork();
        cluster.on('exit', (_, __, ___) => cluster.fork());
    }

    if (cluster.isWorker)
    {
        setTimeout(() => process.exit(1), 5 * 60 * 1000);    // BLACKBOX
        const commands = await list_commands();
        start_bot(commands, process.env.DISCORD_TOKEN);
    }
})();