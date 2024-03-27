#!/usr/bin/node
/**
 * Prints the title of Star Wras movie
 * where the episode number matches a given integer
 */
const request = require('request');

// Get the episode number
const episode = process.argv[2];

//The url
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;

request.get(url).on('response', async function(err, response, body) {
	if (err) {
		console.log(err)
		return;
	}
	const movie = JSON.parse(body);
	console.log(movie.title);
});
