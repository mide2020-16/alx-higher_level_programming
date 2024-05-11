#!/bin/bash
#This script takes URL as input and display the size of
# the body response if the response is 200

if [ -z "$1"]; then
	echo "Usage ./0-body_size.sh <URL>"
	exit 1
fi

