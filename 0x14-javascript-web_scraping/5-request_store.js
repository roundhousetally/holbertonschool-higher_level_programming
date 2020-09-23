#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const savinfile = process.argv[3];
request(url, function (err, response, body) {
  if (err) throw err;
  else {
    fs.writeFile(savinfile, body, 'utf-8', function (err, data) {
      if (err) throw err;
    });
  }
});
