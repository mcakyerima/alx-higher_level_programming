#!/bin/bash

# Use curl to send a GET request and display the body for a 200 status code.
curl -sX GET $1 -L -P 200
