#!/bin/bash
# sends a get request and displays the body of a status 200 response
response_status=$(curl -sI "$1" | grep "HTTP" | cut -d " " -f 2)
if [ $response_status -eq "200" ]; then
    curl -sL "$1"
fi
