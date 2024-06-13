#!/usr/bin/node
/**
 * JavaScript script that fetches and lists the title for all movies by using this URL
 * https://swapi-api.alx-tools.com/api/films/?format=json
 */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (data) {
    const films = data.results;
    films.forEach(function (film) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  }
});
