#!/bin/bash
# sends a request to a url and displays only statsus code of response
curl -sI "$1" | grep "HTTP" | cut -d " "  -f 2
