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

const request = new Request(url);

const response = await fetch(request);
const movie = await response.json();

console.log(movie.title);
