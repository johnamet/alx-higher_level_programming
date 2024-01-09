#!/usr/bin/node
class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number'
        || !Number.isInteger(w) || !Number.isInteger(h)) {
    
    } else {
    this.width = w;
    this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
