#!/bin/bash
# sends a request to a url and displays only statsus code of response
curl -so /dev/null -w "%{http_code}" "$1"
