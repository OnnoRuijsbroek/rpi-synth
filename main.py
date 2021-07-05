#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
from RPi import GPIO  # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
from os import system
import telnetlib
import random

# pins
KEY_PIN = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(KEY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# file
fileName = 'input.txt'
currentRowNumber = 0
maxLinesSourceFile = 189

# cli
prefixInput = 'select 0 1 '
fileInput = '000 000'

host = "127.0.0.1"
port = 9800
timeout = 100


def button_press(self):
    _input_get()
    _input_telnet()
    _input_update()


def _input_get():
    global fileName
    with open(fileName) as f:
        file_row = f.read().splitlines()
    global currentRowNumber
    global fileInput
    fileInput = str(file_row[currentRowNumber])


def _input_telnet():
    with telnetlib.Telnet(host, port, timeout) as session:
        time.sleep(1.0)
        global prefixInput
        global fileInput
        telnetCommand = (str(prefixInput) + str(fileInput) + "\n")
        print(telnetCommand)
        telnetWorkingCommand = "select 0 1 008 004\n"
        session.write(telnetWorkingCommand.encode('ascii'))
        session.read_eager()
        session.close()


def _input_update():
    global currentRowNumber
    currentRowNumber = random.randrange(1, maxLinesSourceFile)


GPIO.add_event_detect(KEY_PIN, GPIO.FALLING, callback=button_press, bouncetime=200)

try:
    while True:
        time.sleep(0.3)
except KeyboardInterrupt:
    GPIO.cleanup()
