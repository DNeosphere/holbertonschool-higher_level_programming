#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = argv[2];

request(url, function (error, response, body) {
  if (error) throw error;

  const toDos = JSON.parse(body);

  const completed = toDos.filter((elem) => elem.completed === true);

  const toDosId = {};
  for (let person = 1; person <= 10; person++) {
    toDosId[person] = (completed.filter((elem) => elem.userId === person)).length;
  }

  console.log(toDosId);
});
