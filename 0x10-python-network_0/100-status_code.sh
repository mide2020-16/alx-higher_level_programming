#!/bin/bash
# Ascript that sends a request to a URL and displays the status codeof the response
curl -sI -w "%{http_code}" "$1" -o /dev/null
