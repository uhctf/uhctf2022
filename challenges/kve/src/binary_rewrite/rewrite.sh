#! /bin/bash

# Quit on errors
set -e

# args:
EMULATION_RESULT_DIR=${1}
FROM_IP=${2}
TO_IP=${3}
FROM_GATEWAY=${4}
TO_GATEWAY=${5}

# binary rewriting of firmware to fix static IP
echo "Rewriting image.raw: ${FROM_IP} -> ${TO_IP}"

# based on:
# - https://unix.stackexchange.com/questions/413664/replace-string-in-a-huge-70gb-one-line-text-file
echo "%option main
%%
${FROM_IP}     printf(\"${TO_IP}\");
%%" > ./rewriter.l
make rewriter
chmod +x ./rewriter
# redirections don't work with sudo so run the command in a new shell
bash -c "./rewriter < ${EMULATION_RESULT_DIR}image.raw > ${EMULATION_RESULT_DIR}image.raw.new"
# also, put output in a new file as reading/writing from the same just creates an empty file
mv ${EMULATION_RESULT_DIR}image.raw.new ${EMULATION_RESULT_DIR}image.raw
chown root:root ${EMULATION_RESULT_DIR}image.raw

# rewriting of emulation config
echo "Rewriting emulation config: ${FROM_GATEWAY} -> ${TO_GATEWAY}"
sed "s/${FROM_GATEWAY}/${TO_GATEWAY}/g" ${EMULATION_RESULT_DIR}/run.sh -i
chown root:root ${EMULATION_RESULT_DIR}/run.sh
sed "s/${FROM_IP}/${TO_IP}/g" ${EMULATION_RESULT_DIR}ip* -i
chown root:root ${EMULATION_RESULT_DIR}ip*
