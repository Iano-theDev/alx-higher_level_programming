#!/bin/bash
# sends a post request to a url passed as a variable with given url paramaters
curl -sX POST -d "email=test@gmail.com&wsubject=I will always be here for PLD" "$1"
