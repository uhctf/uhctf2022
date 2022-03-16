#! /bin/bash

TEMPFILE=`mktemp`

# 1. compile statically so it's big enough for UPX to compress
# 2. no compiler optimisations to keep decompiled binary simple and ensure unused string is not removed
gcc ./src/main.c -o ${TEMPFILE} -O0 -static

# pack with UPX
upx -9 ${TEMPFILE}

# tweak magic bytes
mkdir -p ./attachments/
xxd -p ${TEMPFILE} | /usr/bin/sed '8s/555058/4d5349/' | xxd -p -r > ./attachments/MSI
chmod +x ./attachments/MSI

rm ${TEMPFILE}
echo 'Check the `./attachments` directory'