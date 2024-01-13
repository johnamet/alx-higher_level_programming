#!/usr/bin/node
const findSecondMax = (...args) => {
  if (args.length <= 1) {
    console.log(0);
    return;
  }
  const integers = args.map(Number).filter(Number.isInteger);

  if (integers.length <= 1) {
    console.log(0);
    return;
  }

  const sortedIntegers = integers.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
};

const [, , ...args] = process.argv;

findSecondMax(...args);
