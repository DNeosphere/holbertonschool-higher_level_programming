#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = argv[2];

request(url, function (error, response, body) {
  if (error) throw error;

  const charList = [];
  const films = JSON.parse(body).results;

  for (const film of films) {
    const characters = film.characters;
    for (const person of characters) {
      if (person.includes('18')) {
        charList.push(person);
      }
    }
  }
  console.log(charList.length);
});
