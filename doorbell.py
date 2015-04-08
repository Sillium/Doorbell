#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import gmtime, strftime, sleep
from datetime import datetime
import RPi.GPIO as GPIO
import os
import subprocess
import os.path
import httplib, urllib
import atexit
import traceback
import logging
import time

# Logging
logger = logging.getLogger('doorbell')
hdlr = logging.FileHandler('doorbell.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

# Start
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " Doorbell started")
logger.info("Doorbell started")

# Volume
#cmdVolume='amixer set PCM -- 1000'
#subprocess.call(cmdVolume, shell=True)

# Pins
GPIO.setmode(GPIO.BOARD)

led_list = [15,16,26,24]
#relais_list = [13]

GPIO.setup(led_list, GPIO.OUT, initial=0)   # alle an
#GPIO.setup(relais_list, GPIO.OUT, initial=0) # beide aus
GPIO.setup(12, GPIO.IN)

time.sleep(1)

GPIO.output(15, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
#GPIO.output(18, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)

# Loop
while 1:
    if GPIO.input(12) == GPIO.LOW:
        print("--> Taster gedrueckt")
        logger.info("--> Taster gedrueckt")
	
	# Switch on LED
        GPIO.output(15, GPIO.LOW)
        try:
            # Setup
            now=strftime("%Y-%m-%d %H:%M:%S", gmtime())
            
            # Pushover
            print("--> Pushover")
            logger.info("--> Pushover")
            conn = httplib.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
                urllib.urlencode({
                            "token": "xxx", # app
                            "user": "yyy", # user group/user
                            "message": "Dingdong!",
                            "url": "http://192.168.66.6/dooropener.php",
                            "url_title": "Tür öffnen!"
                          }),
                    { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()
            
            # Finished
            print("--> Finished")
            logger.info("--> Finished")
            time.sleep(2)
        
        except Exception, e:
            traceback.print_exc()
            logging.exception("!!!")
        
        # Switch off LED
	GPIO.output(15, GPIO.HIGH)
    else:
        GPIO.output(16, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(16, GPIO.HIGH)
        time.sleep(0.1)

GPIO.cleanup()
