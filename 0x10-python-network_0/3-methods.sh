#!/bin/bash
# Displays all HTTP methods allowed for a URL
curl -sIX OPTIONS | grep "Allowed:" | cut -d " " -f 2-
