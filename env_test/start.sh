#!/bin/sh
# Add your startup script

# DO NOT DELETE

service apache2 start;
socat tcp-listen:9999,fork exec:/home/ctf/bin &
sleep infinity;
