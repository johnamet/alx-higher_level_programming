#!/usr/bin/node
const [, , arg] = process.argv;

if (arg !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
