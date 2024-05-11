#!/bin/bash
# A script that displays all the allowed method a servwer can process
curl -sI "$1" | grep -i "Allow" | cut -d " " -f2-
