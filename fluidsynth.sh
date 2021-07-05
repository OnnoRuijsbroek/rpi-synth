#!/bin/bash

if pgrep -x "fluidsynth" > /dev/null
then
echo fluidsynth already running
else
mpg321 startup.mp3
sleep 4
fluidsynth  -si -p "fluid" -C0 -R0 -r48000 -d -f ./config.txt -a alsa -m alsa_seq &
sleep 8 # wait for fluidsynth to load e.g. config.txt
fi

lpk25=$(aconnect -o | grep "LPK25")

if [[ $lpk25 ]]
then
aconnect 'LPK25':0 'fluid':0
echo LPK25 connected
else
echo No known midi devices available. Try aconnect -l
fi

echo RASPI-SYNTH startig telnet
sudo python3 /home/pi/main.py&
telnet 127.0.01 9800