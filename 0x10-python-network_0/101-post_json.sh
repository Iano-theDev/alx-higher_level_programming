#!/bin/bash
# sends a json post request to a URL passed as the first argument
curl -X POST -H "Content-Type: application/json"  -d "$2" "$1"
