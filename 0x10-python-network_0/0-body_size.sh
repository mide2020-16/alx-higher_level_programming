#!/bin/bash
#This script takes URL as input and display the size of the body response

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

response=$(curl -s -o /tmp/body_size "$1")

if [ $? -ne 0 ]; then
	echo "Error: Unable to get a response from $1"
	exit 1
fi

body_size=$(stat -c %s /tmp/body_size)

echo "$body_size"
