#!/usr/bin/node

const argv = process.argv;
const numA = parseInt(argv[2]);

function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (isNaN(numA)) {
  console.log(1);
} else {
  console.log(factorial(numA));
}
