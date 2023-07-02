#!/bin/bash
# Displays all HTTP methods allowed for a URL
curl -sIX OPTIONS $1 | grep "Allowed:" | cut -d " " -f 2-
