#! /bin/bash

# Quit on errors
set -e

# Set env vars
ORIG_PWD=`pwd`/
DEVICE_PATH=`pwd`/device/

cd ./FirmAE/
./init.sh

# Pre-build firmware
set +e
sudo ./run.sh -c `cat ${DEVICE_PATH}brand` ${DEVICE_PATH}firmware.zip
set -e

echo IID=`./scripts/util.py get_iid ${DEVICE_PATH}firmware.zip 127.0.0.1` > ${ORIG_PWD}.env
echo FROM_IP=`cat ${DEVICE_PATH}from_ip` >> ${ORIG_PWD}.env
echo FROM_GATEWAY=`cat ${DEVICE_PATH}from_gateway` >> ${ORIG_PWD}.env

cd ${ORIG_PWD}
sudo docker-compose up
