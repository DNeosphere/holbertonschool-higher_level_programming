#!/usr/bin/node

let len = 0;
for (len in process.argv) {
  len++;
}

if (len > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
