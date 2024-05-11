#!/bin/bash
# Ascript that dispalys a custom message
curl -s -w "You got me!" -o /dev/null 0.0.0.0:5000/catch_me
