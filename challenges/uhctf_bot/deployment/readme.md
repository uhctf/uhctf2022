# Deployment
1. Create an application with a bot over at https://discord.com/developers/applications/
2. Copy `default.env` to `src/.env` and fill in the values
    - For `DISCORD_CLIENT_ID` and `DISCORD_TOKEN` see the OAuth2 tab for your application
    - `DISCORD_GUILD_ID` is the ID of the server which the bot will be invited to
w. Invite bot to your server: https://discord.com/oauth2/authorize?scope=applications.commands+bot&permissions=1024&client_id=<client_id>
4. `docker build -t <image_name> .`
5. `docker run --rm <image_name>`