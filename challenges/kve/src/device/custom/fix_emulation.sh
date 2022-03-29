#! /firmadyne/sh

BUSYBOX=/firmadyne/busybox

# default gateway setup
${BUSYBOX} ip route delete default || true
${BUSYBOX} ip route add default via <gateway>

# DNS setup
echo 'nameserver 8.8.8.8' > /etc/resolv.conf
echo 'nameserver 8.8.4.4' >> /etc/resolv.conf

# replace FW's busybox with FirmAE's busybox, to give adversaries more tools to play with. Letting them download stuff over the highly limited bandwidth of the emulated network would potentially annoy them and decrease retention rate.
cp ${BUSYBOX} /bin/busybox

# tweak available binaries
ln -s ../../bin/busybox /usr/sbin/nc
ln -s ../../bin/busybox /usr/sbin/telnet
for bin in /sbin/halt /bin/kill /usr/bin/killall /sbin/poweroff /usr/sbin/telnetd /usr/bin/tftp /bin/umount
do
    ${BUSYBOX} unlink ${bin}
done

# disable ASLR. Based on the PoC's working, the original EX6100v1 has this disabled as well.
echo -n 0 > /proc/sys/kernel/randomize_va_space

# write flag
echo 'uhctf{ez-bo-cve-ftw-c6e2ff}' > /flag.txt
