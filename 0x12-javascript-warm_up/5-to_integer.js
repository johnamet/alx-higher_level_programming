#!/usr/bin/node
const [, , arg1] = process.argv;

const myNumber = parseInt(arg1);

if (!isNaN(myNumber)) {
  console.log(`My number: ${myNumber}`);
} else {
  console.log('Not a number');
}
