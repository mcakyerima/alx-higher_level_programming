#!/bin/bash

# Use curl to send a GET request and display the body for a 200 status code.
curl -s -X GET -w "{http_code} "S1" | {
	read -r status
	if [ "$status" -eq 200 ]; then
			curn -s "$1"
	else
		echo 'Error: HTTP status $Status"
	fi
}
