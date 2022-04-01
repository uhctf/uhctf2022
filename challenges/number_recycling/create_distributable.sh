#! /bin/bash

DIR=`mktemp -d`

cd ./src/
virtualenv ./tmpenv
source ./tmpenv/bin/activate
pip install -r requirements.txt
python ./main.py ${DIR}
rm -rf ./tmpenv
cd -

mkdir -p ./attachments/
zip -mr ./attachments/number_recycling.zip ${DIR}
echo 'Check `./attachments` directory'