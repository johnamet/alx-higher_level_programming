#!/usr/bin/node
/**
 * Prints the title of Star Wars movie
 * where the episode number matches a given integer
 */
const request = require('request');

// Get the episode number from command-line arguments
const episode = process.argv[2];

// The URL
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;

// Send a GET request to the Star Wars API
request.get(url, function (error, response, body) {
  // Parse the response body as JSON
  const movie = JSON.parse(body);
  console.log(movie.title);
});
