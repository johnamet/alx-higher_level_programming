#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -LX PUT -H "Content-Type: text/plain" -d "This is the contents of my text file." http://0.0.0.0:5000/catch_me
