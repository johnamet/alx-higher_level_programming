#!/usr/bin/node
const [, , arg1] = process.argv;

const myNumber = parseInt(arg1);
let i = 0;

if (isNaN(myNumber)) {
  console.log('Missing number of occurences');
} else {
  while (i !== myNumber) {
    console.log('C is fun');
    i += 1;
  }
}
