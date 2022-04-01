#! /bin/bash

set -e

# Install latest docker-compose (`apt` is behind several versions)
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install FirmAE IoT emulation framework
git clone --recursive https://github.com/pr0v3rbs/FirmAE
cp -r ./FirmAE_custom/* ./FirmAE/
cd ./FirmAE/
./download.sh
./install.sh
sudo ./docker-init.sh

cd -
sudo apt-get --yes clean
