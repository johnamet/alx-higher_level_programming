#!/bin/bash
# the script takes a url and sends rquest to display the size of the body

curl -sI "$1" | grep Content-Length | awk '{print $2}'
