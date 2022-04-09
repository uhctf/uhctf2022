#!/bin/sh
# Script to setup the challenge from a scratch Alpine Linux VM/Docker
set -e

# Install Python to make the database
apk add --no-cache python3 sqlite p7zip py3-virtualenv

# Create the database contents
python3 database/convert.py

# Setup a virtualenvironment
python3 -m virtualenv webserver/venv
source webserver/venv/bin/activate
pip install -r requirements.txt

# Build the frontend
set +e
rm -R static
set -e

apk add --no-cache nodejs npm
cd frontend
npm install
npm install -g @vue/cli
npx vue build
cd ..
mv frontend/dist ./webserver/static

# Save some space
rm -R frontend/node_modules
apk del npm nodejs p7zip

echo "Ready to deploy"
