#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');

fs.writeFile(argv[2], argv[3], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
