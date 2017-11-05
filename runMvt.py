#!/usr/bin/env python
import time
import urllib2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pir = 5
pled = 12
GPIO.setup(pir, GPIO.IN)
GPIO.setup(pled, GPIO.OUT)
jeedomurl = "http://127.0.0.1/core/api/jeeApi.php?apikey=mEiBkSqJI730kLBC7yUTFaR5FYXaS5meYmFieVJNskmvNNWsdIkIITcnRSpBvtGk7uk4gUg1WtKJX9SagUBHO6U8wihHtNJHYUiXOgwC1Xlw6dp4PHi6kdb9dafpFPV6BV3ybFR2CcEXXKsM22rCvjarbf7GM2jwv5Cnh47C6i2tLIXkinE5pEKqKgV7yWSB15O9Otaju25ei2pr7TCK8nRhuE7JAxkRIZq7sq95Ga9OsFWN92yVEgVPK21tFBj"
jeedomcmdid = "183"
lastvalue = -1
while True:
    if (GPIO.input(pir)):
        # mouvement
        if (lastvalue != 1):
            #print("1")
            GPIO.output(pled, GPIO.HIGH)
            f = urllib2.urlopen(jeedomurl + "&type=virtual&id=" + jeedomcmdid + "&value=true")
            f.read()
            f.close()
        lastvalue = 1
    else:
        # pas de mouvement
        if (lastvalue != 0):
            #print("0")
            GPIO.output(pled, GPIO.LOW)
            f = urllib2.urlopen(jeedomurl + "&type=virtual&id=" + jeedomcmdid + "&value=false")
            f.read()
            f.close()
        lastvalue = 0
    time.sleep(0.5)
