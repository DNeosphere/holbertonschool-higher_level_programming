#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = `http://swapi.co/api/films/${argv[2]}`;

request(url, function (err, response, body) {
  if (err) throw err;

  console.log(`${JSON.parse(body).title}`);
});
