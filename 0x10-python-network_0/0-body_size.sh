#!/bin/bash
#This script takes URL as input and display the size of the body response
echo "$(curl -s -o /tmp/body_size "$1" | stat -c %s /tmp/body_size)"
