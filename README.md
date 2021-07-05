# rpi-synth

Raspberry pi with midi synthesizer. Instrument changes by the push of a physical button. 
   Inspired by https://lucidbeaming.com/blog/running-fluidsynth-on-a-raspberry-pi-zero-w/ though opted out for usage of a screen.
    
## os and basics
- install headless linux
- sudo apt-get update | sudo apt-get upgrade
- sudo apt-get install python3-smbus python3-dev python3-rpi.gpio python3-pip libopenjp2-7 libtiff5 #python script
- sudo apt-get install mpg321 #audio player used during boot
- copy over files
   - fluidsynth.sh, script to fluidsynth and its prerequisites
   - input.txt, content of the fluidsynth sound bank (specific per loaded file) for usage in python script
   - main.py, python script for button changing instrument
   - confix.txt, fluidsynth config file (to get specific list: `echo "inst 1" | fluidsynth /usr/share/sounds/sf2/FluidR3_GM.sf2`)

## install (newer) fluidsynth
- https://github.com/albedozero/fluidpatcher/wiki/Programs
   - git clone https://github.com/FluidSynth/fluidsynth.git
   - sudo apt update
   - sudo apt build-dep fluidsynth --no-install-recommends
   - mkdir fluidsynth/build
   - cd fluidsynth/build
   - cmake ..
   - make
   - sudo make install
   - sudo ldconfig
- sudo apt-get install fluid-soundfont-gm # soundbank of instruments, you can use different one

## audio tweaks
- nano /boot/config.txt -> comment out #dtparam=audio=on
- increase responsiveness
   - sudo usermod -a -G audio pi
   - sudo nano /etc/security/limits.d/audio.conf
     ```@audio - rtprio 80
        @audio - memlock unlimited```
- set usb audio to default
 - sudo nano /etc/asound.conf
   ```pcm.!default {
       type hw card Device
                 }
       ctl.!default {
       type hw card Device
       }```
- test audio
   - sudo reboot
   - aplay -l
   - lsusb -t
   - speaker-test -c2 -twav

## fluidsynth boot script
- sudo chmod a+x fluidsynth.sh
- sudo nano .bash_profile -> add `./fluidsynth.sh`