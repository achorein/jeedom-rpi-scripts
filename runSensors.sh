#!/bin/bash

if [ `whoami` != "root" ];then
	echo "Must be root to execute this script"
	exit
fi

NOW=$(date +'%x %X')
TMP36=$(/opt/jeedom-rpi-scripts/readTempTMP36.py)
LDR=$(/opt/jeedom-rpi-scripts/readLDR.py)

echo "{\"TMP36\": $TMP36, \"LDR\": $LDR, \"date\": \"$NOW\"}" > /var/www/html/sensors.json

API_KEY="CHANGE_IT"
JEEDOM_URL="http://domotique:80"
curl "$JEEDOM_URL/core/api/jeeApi.php?plugin=virtual&apikey=$API_KEY&type=virtual&id=191&value=$TMP36"
curl "$JEEDOM_URL/core/api/jeeApi.php?plugin=virtual&apikey=$API_KEY&type=virtual&id=193&value=$LDR"
