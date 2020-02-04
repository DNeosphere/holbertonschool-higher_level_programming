#!/usr/bin/node

const argv = process.argv;
const intNumber = parseInt(argv[2]);

if (isNaN(intNumber)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < intNumber; i++) {
    console.log('C is fun');
  }
}
