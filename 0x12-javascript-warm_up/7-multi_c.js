#!/usr/bin/node
const therayray = 'C is fun';
if (process.argv[2] > 0) {
  for (let i = 0; i < process.argv[2]; i++) { console.log(therayray); }
} else {
  console.log('Missing number of occurences');
}
if (process.argv[2] < 0) {
}
