#!/bin/bash

if [ -f /tmp/jeedom_gpio.run ];then
	echo "`date` | erreur $0" >> /tmp/jeedom_gpio.log
	exit
fi
echo "$0" > /tmp/jeedom_gpio.run

sudo /opt/scripts/readTempTMP36.py

rm /tmp/jeedom_gpio.run
