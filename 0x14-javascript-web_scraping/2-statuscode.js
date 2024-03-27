#!/usr/bin/node
/**
 * The script displays the status code of a GET request
 */
const request = require('request');

// Get the url
const url = process.argv[2];

// send a get request
request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
