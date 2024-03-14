#!/usr/bin/node

let numberOfArgs = 0;
exports.logMe = function (item) {
  console.log(numberOfArgs + ': ' + item);
  numberOfArgs += 1;
};
