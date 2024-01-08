#!/usr/bin/node
const { argv } = require('node:process');

const passedArgs = argv.slice(2);

if (passedArgs.length === 0) {
  console.log('No argument');
} else {
  passedArgs.forEach((value, _) => {
    console.log(`${value}`);
  });
}
