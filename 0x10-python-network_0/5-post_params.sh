#!/bin/bash
# Sends a POST request to a URL with POST data
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
