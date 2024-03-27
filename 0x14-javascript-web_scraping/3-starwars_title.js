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
request.get(url, function(error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log(response);
//   // Parse the response body as JSON
     const movie = JSON.parse(body);
  console.log(movie);
//   // Print the title of the movie
//   console.log(movie.title);
});
