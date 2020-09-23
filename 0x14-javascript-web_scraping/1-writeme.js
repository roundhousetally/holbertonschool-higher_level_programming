#!/usr/bin/node
const fs = require('fs');
const fi = process.argv[2];
const data = process.argv[3];
fs.writeFile(fi, data, (err) => {
  if (err) throw err;
});
