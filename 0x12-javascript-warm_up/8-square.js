#!/usr/bin/node
const [, , arg1] = process.argv;

const myNumber = parseInt(arg1);
let i = 0;

if (isNaN(myNumber)) {
  console.log('Missing size');
} else {
  if (myNumber > 0) {
    while (i !== myNumber) {
      let width = '';
      for (let j = 0; j < myNumber; j++) {
        width += 'X';
      }
      console.log(`${width}`);
      i += 1;
    }
  }
}
