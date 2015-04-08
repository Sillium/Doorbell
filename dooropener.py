#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

# RPi.GPIO Layout verwenden (wie Pin-Nummern)
GPIO.setmode(GPIO.BOARD)

led = 18
relais = 11

# LED und Relais an
GPIO.setup(led, GPIO.OUT, initial=0)
GPIO.setup(relais, GPIO.OUT, initial=1)

time.sleep(3)

# Relais und LED wieder aus
GPIO.output(relais, GPIO.LOW)
GPIO.output(led, GPIO.HIGH)

GPIO.cleanup()
