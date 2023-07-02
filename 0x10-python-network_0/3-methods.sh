#!/bin/bash
# Displays all HTTP methods allowed for a URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
