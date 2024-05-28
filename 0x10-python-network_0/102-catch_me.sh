#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me to respond with a message containing You got me!
curl -sX PUT -H "You got me!" 0.0.0.0:5000/catch_me
