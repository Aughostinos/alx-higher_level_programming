#!/usr/bin/node
/**
 * This script prints the title of a Star Wars movie where the episode number matches a given integer.
 */

const request = require('request');
const movie_id = process.argv[2];
const api_url = 'https://swapi-api.alx-tools.com/api/films/${movie_id}';

request.get(api_url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title)
  }
});