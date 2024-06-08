#!/usr/bin/node
/**
 * this script writes a string to a file.
 */

const fs = require('fs');
const filePath = process.argv[2];
const string_to_write = process.arv[3]

fs.writeFile(filePath, string_to_write, 'utf8', (err) => {
  if (err) {
    console.log(err);
    return;
  }
});