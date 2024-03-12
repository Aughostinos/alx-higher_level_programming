#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n <= 0) { // Base case for NaN or non-positive numbers
    return 1;
  } else if (n === 1) { // Base case for factorial
    return 1;
  } else {
    return n * factorial(n - 1); // Recursive step
  }
}

const n = parseInt(process.argv[2]);

console.log(factorial(n));
