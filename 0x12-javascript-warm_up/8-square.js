#!/usr/bin/node

const argv = process.argv;
const intNumber = parseInt(argv[2]);

if (isNaN(intNumber)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < intNumber; i++) {
    console.log('X'.repeat(intNumber));
  }
}
