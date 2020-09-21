#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
