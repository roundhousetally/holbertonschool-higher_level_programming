#!/usr/bin/node
const num = process.argv;
if (num.length < 4) {
  console.log('0');
} else {
  console.log(num.sort().reverse()[1]);
}
