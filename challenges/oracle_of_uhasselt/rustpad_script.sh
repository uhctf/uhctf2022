#! /bin/bash

echo ${1} | nc 127.0.0.1 2323 | grep 'The oracle understands your struggles...'