#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -sL -X POST -H "Content-Type: application/json" -d '{"message": "I am coming for you!"}' http://0.0.0.0:5000/catch_me
