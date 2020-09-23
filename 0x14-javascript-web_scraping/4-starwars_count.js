#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    let f = 0;
    let c = 0;
    for (f; f < films.length; f++) {
      for (c; c < films[f].characters.length; c++) {
        if (films[f].characters[c].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
