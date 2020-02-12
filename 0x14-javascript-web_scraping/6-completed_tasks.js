#!/usr/bin/node

const url = process.argv[2];
const req = require('request');

req(url, (err, res, body) => {
  if (err) console.log(err);
  const completed = {};
  const obj = JSON.parse(body);
  for (const i in obj) {
    const task = obj[i];
    const userID = obj[i].userId;

    if (task.completed) {
      if (completed[userID] === undefined) {
        completed[userID] = 1;
      } else {
        completed[userID] += 1;
      }
    }
  }
  console.log(completed);
});
