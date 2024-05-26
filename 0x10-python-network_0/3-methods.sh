#!/bin/bash
# displays all http verbs a url accepts
curl -sI "$1" | grep "Allow" | cut -d ":" -f 2 | xargs 
