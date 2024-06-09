#!/usr/bin/node
/**
 * This script prints the number of movies where the character "Wedge Antilles" is present.
 */

const request = require('request');
const apiUrl = process.argv[2];
const characterUrl = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:', response.statusCode);
    return;
  }

  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;

  films.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterUrl}/`)) {
      count++;
    }
  });

  console.log(count);
});
