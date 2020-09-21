#!/usr/bin/node
class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let x = 0; x < this.width; x++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
