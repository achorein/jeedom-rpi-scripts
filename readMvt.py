#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pir = 5
pled = 12
GPIO.setup(pir, GPIO.IN)
GPIO.setup(pled, GPIO.OUT)
if (GPIO.input(pir)):
    print("1")
    GPIO.output(pled, GPIO.HIGH)
    # mouvement
else:
    print("0")
    # pas de mouvement
    GPIO.output(pled, GPIO.LOW)
