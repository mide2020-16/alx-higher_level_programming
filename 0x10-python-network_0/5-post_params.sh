#!/bin/bash
# A script that sends a POST request to the URL
curl -sX POST --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
