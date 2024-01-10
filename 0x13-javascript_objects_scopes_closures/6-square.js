#!/usr/bin/node
const Sq = require('./5-square');
class Square extends Sq {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
