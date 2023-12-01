#!/bin/bash
# Acceps a URL, sends a DELETE request using curl and displays response body
curl -sX DELETE "$1"
