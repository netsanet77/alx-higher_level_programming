#!/usr/bin/node
const oldSquare = require('./5-square.js');

class Square extends oldSquare {
  charPrint (c) {
    super.print(c);
  }
}
module.exports = Square;
