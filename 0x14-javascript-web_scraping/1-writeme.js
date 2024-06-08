#!/usr/bin/node
/**
 * this script writes a string to a file.
 */

const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3]

fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.log(err);
    return;
  }
});
