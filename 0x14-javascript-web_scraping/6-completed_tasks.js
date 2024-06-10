#!/usr/bin/node
/**
 * This script prints the number of movies where the character "Wedge Antilles" is present.
 */

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body).results;
  const completedTask = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if(completedTask[todo.userId]) {
        completedTask[todo.userId]++;
      } else {
        completedTask[todo.userId] = 1;
      }
    }
  });
  console.log(completedTask);
});