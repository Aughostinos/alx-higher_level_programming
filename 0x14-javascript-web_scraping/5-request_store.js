#!/usr/bin/node
/**
 * this script writes a string to a file.
 */

const fs = require('fs');
const url = process.argv[2]
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if(error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
        return;
      }
  });
}
});
