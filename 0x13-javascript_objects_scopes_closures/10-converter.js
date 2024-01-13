#!/usr/bin/node
exports.converter = function (base) {
  const convertRecursive = (decimalNumber) => {
    if (decimalNumber === 0) {
      return '';
    } else {
      return convertRecursive(Math.floor(decimalNumber / base)) + (decimalNumber % base).toString(base);
    }
  };

  return (decimalNumber) => convertRecursive(decimalNumber);
};
