#! /bin/bash

cd ./src/

DIR=`mktemp -d`
cp -r ./commands/ ${DIR}
cp ./bot.js ${DIR}
cp ./index.js ${DIR}
cp ./package.json ${DIR}
cp ./package-lock.json ${DIR}

# remove blackbox code lines
/usr/bin/sed -i "/BLACKBOX/d" ${DIR}/*.js
/usr/bin/sed -i "/BLACKBOX/d" ${DIR}/**/*

cd -

zip -mr ./attachments/prototype_discord_bot.zip ${DIR}
echo 'Check `./attachments` directory'
