#!/usr/bin/node

const argv = process.argv;
const numA = parseInt(argv[2]);
const numB = parseInt(argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(numA, numB);
