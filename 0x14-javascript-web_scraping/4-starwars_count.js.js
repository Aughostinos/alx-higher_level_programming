#!/usr/bin/node
/**
 * This script prints the number of movies where the character "Wedge Antilles" is present.
 */

const request = require('request');
const apiUrL = process.argv[2];
const characterId = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).result;
    const count = films.reduce((acc, film) => {
      if (film.characters.includes(characterUrl)){
        acc ++;
      }
      return acc;
    },0);
    console.log(count);
  }
});
