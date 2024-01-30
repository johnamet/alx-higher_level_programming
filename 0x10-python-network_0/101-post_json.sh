#!/bin/bash
# the script posts json file
curl -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
