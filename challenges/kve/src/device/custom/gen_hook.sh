#! /bin/bash

# This script is called during init of the emulated firmware.
# See \`FirmAE_custom/scripts/makeImage.sh\` and \`makeNetwork.py\` for more details.
echo "#! /firmadyne/sh

# tweak emulated FW to be usable
(sleep 180 && /firmadyne/fix_emulation.sh) &
(sleep 210 && /firmadyne/fix_emulation.sh) &
(sleep 240 && /firmadyne/fix_emulation.sh) &

while [[ 1 ]]
do
    # upnpd is a daemon
    /usr/sbin/upnpd &>/dev/null
    sleep 3
    kill -9 \`/firmadyne/busybox netstat -ltpn | grep 5000 | /firmadyne/busybox cut -d' ' -f 45 | grep -v netstat | /firmadyne/busybox cut -d'/' -f1\`
done
" > /work/custom/hook.sh

chmod a+x /work/custom/hook.sh
