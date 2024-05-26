#!/bin/bash
# displays all http verbs a url accepts
curl -I "$1" | grep "Allow" | cut -d ":" -f 2 | xargs 
