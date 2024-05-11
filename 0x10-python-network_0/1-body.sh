#!/bin/bash
#This script takes URL as input and display the size of the body response if the response is 200
curl -s -o /tmp/body -w "%{http_code}" "$1" > /dev/null && (status_code=$(cat /tmp/body); [ "$status_code" -eq 200 ] && cat /tmp/body)
