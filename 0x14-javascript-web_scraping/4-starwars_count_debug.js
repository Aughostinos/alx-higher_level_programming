#!/usr/bin/node
/**
 * This script prints the number of movies where the character "Wedge Antilles" is present.
 */

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

console.log('API URL:', apiUrl);
console.log('Character URL:', characterUrl);

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    let films;
    try {
      films = JSON.parse(body).results; // Correctly assign parsed results to films
      console.log('Films:', films);
    } catch (parseError) {
      console.error('Parsing Error:', parseError);
      return;
    }

    const count = films.reduce((acc, film) => {
      console.log(`Checking film: ${film.title}`);
      console.log('Characters in film:', film.characters);

      if (film.characters.includes(characterUrl)) { // Correctly use characterUrl
        console.log(`Character found in film: ${film.title}`);
        acc++;
      }
      return acc;
    }, 0);
    
    console.log('Count:', count);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
