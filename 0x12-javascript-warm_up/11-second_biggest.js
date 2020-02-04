#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const nArray = argv.slice(2, argv.length);
  nArray.sort();
  const n = nArray.pop();
  if (n === nArray[nArray.length - 1]) {
    nArray.pop();
  }
  console.log(nArray[nArray.length - 1]);
}
