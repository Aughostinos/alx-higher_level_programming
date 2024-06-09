#!/usr/bin/node
/**
 * This script prints the number of movies where the character "Wedge Antilles" is present.
 */

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;
const characterUrl = `http://swapi.co/api/people/${characterId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    let films;
    try {
      JSON.parse(body).results;
    } catch (parseError) {
      console.error('parsing Error:', parseError);
      return;
    }
    const count = films.reduce((acc, film) => {
      if (film.characters.includes(film.characterUrl)) {
        acc++;
      }
      return acc;
    }, 0);
    console.log(count);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
