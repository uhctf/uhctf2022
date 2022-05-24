#! /bin/bash

echo ${1} | nc 127.0.0.1 420 | /usr/bin/grep 'The oracle understands your struggles...' >/dev/null
