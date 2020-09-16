#!/usr/bin/node
const therayray = 'C is fun';
const arg = (parseInt(process.argv[2]));
if (isNaN(arg)) {
  console.log('Missing number of occurences');
}
if (arg < 0) {
}
if (parseInt(process.argv[2]) > 0) {
  for (let i = 0; i < process.argv[2]; i++) { console.log(therayray); }
}
