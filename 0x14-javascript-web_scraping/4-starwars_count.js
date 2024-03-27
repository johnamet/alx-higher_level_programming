#!/usr/bin/node
/**
 * Prints the title of Star Wars movie
 * where the episode number matches a given integer
 */
const request = require('request');

// The URL
const url = 'https://swapi-api.alx-tools.com/api/films/';

// Send a GET request to the Star Wars API
request.get(url, function (error, response, body) {
  if (error) {
    return;
  }
  // Parse the response body as JSON
  const movieJson = JSON.parse(body);
  const results = movieJson.results;

  const filterd = results.map(movie => movie.characters.filter(url => url.endsWith('/18/')))
    .filter(movie => movie.length > 0);

  console.log(filterd.length);
});
