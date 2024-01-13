#!/usr/bin/node
function add (a, b) {
  const result = a + b;
  return result;
}

const [, , arg1, arg2] = process.argv;
const fArg = parseInt(arg1);
const sArg = parseInt(arg2);

const result = add(fArg, sArg);

console.log(`${result}`);
