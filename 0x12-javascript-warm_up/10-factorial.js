#!/usr/bin/node
function factorial (a) {
  let result = a;
  if (a === 0 || isNaN(a)) {
    result = 1;
  } else if (a > 0) {
    result *= factorial(a - 1);
  }
  return result;
}

const [, , arg1] = process.argv;
const fArg = parseInt(arg1);

const result = factorial(fArg);

console.log(`${result}`);
