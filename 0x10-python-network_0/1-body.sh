#!/bin/bash
# Takes URL sends a GET requst and displays the body of the response
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && cat

