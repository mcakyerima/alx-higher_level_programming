#!/bin/bash
# Accepts a URL, then display body of a 200 response; Usage: ./1-body.sh 5B0.0.0.0:5000/route_1 ; echo ""
curl -sL "$1"
