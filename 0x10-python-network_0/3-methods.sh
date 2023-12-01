#!/bin/bash
# Takes in a URL, and displays all the HTTP METHODS THE SERVER accepts
curl -sI "$1" | grep -i 'Allow:' | awk '{print substr($0, index($0, $2))}'
