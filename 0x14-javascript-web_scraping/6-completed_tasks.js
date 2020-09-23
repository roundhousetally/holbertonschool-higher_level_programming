#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const bod = JSON.parse(body);
    const dict = {};
    for (const i in bod) {
      const thistask = bod[i];
      if (thistask.completed === true) {
        if (dict[thistask.userId] === undefined) {
          dict[thistask.userId] = 1;
        } else {
          dict[thistask.userId]++;
        }
      }
    }
    console.log(dict);
  }
});
