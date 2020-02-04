#!/usr/bin/node

const argv = process.argv;
const intNumber = parseInt(argv[2]);

if (isNaN(intNumber)) {
  console.log('Not a number');
} else {
  console.log('My number:', intNumber);
}
