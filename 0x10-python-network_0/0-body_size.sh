#!/bin/bash
#This script takes URL as input and display the size of the body response
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2
