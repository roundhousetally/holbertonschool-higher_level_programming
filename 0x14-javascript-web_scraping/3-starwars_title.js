#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else (response.statusCode === 200);
  console.log(JSON.parse(body).title);
});
