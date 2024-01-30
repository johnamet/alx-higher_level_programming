#!/bin/bash
# the script posts json file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
