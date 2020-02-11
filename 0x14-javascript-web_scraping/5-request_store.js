#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = argv[2];
const fileName = argv[3];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) throw error;

  fs.writeFile(fileName, body, 'utf-8', function (err) {
    if (err) throw err;
  });
});
