#!/usr/bin/node
const fs = require('fs');
const fi = process.argv[2];
fs.readFile(fi, 'utf-8', (err, data) => {
  if (data != null) {
    console.log(data, '\n');
  } else {
    console.error(err);
  }
});
