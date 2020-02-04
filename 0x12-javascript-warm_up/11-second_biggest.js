#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const nArray = argv.slice(2, argv.length);

  nArray.sort(function (a, b) { return a - b; });
  const uArray = [...new Set(nArray)];
  console.log(uArray);
  uArray.pop();
  console.log(uArray[uArray.length - 1]);
}
