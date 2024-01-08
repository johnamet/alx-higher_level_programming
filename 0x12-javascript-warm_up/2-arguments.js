#!/usr/bin/node
const { argv } = require('node:process');

const passedArgs = argv.slice(2);

if (passedArgs.length === 0) {
  console.log('No argument');
} else if (passedArgs.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
