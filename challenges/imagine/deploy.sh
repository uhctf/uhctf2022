#! /bin/bash

cd ./src
sudo docker build -t imagine .
cd -
sudo docker image save imagine > ./attachments/imagine_docker.tar
sudo docker image rm imagine