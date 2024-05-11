#!/bin/bash
# A script that POST a json data to the server
curl -s "$1" -d@"$2" -H "Content-Type :application/json"
