#!/bin/bash
# the script posts json file
curl -H "Content-Type: application/json" -d @"$2" "$1"
