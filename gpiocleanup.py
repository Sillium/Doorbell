import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
led_list = [15,16,18,24,26]
relais_list = [11,13]
GPIO.setup(led_list, GPIO.OUT, initial=1)   # alle an
GPIO.setup(relais_list, GPIO.OUT, initial=0) # beide aus
GPIO.setup(12,GPIO.IN)
GPIO.cleanup()
