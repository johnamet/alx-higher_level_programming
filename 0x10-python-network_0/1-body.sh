#!/usr/bin/env bash
# Takes URL sends a GET requst and displays the body of the response
if [ $(curl -s -o /dev/null -w "%{http_code}" "$1") -eq 200 ]; then curl -s "$1"; fi;

