#!/usr/bin/node

const args = process.argv.slice(2);

const sortedArgs = args.sort((a, b) => a - b);

if (sortedArgs.length < 2) {
  console.log(0);
} else {
  console.log(sortedArgs[sortedArgs.length - 2]);
}
