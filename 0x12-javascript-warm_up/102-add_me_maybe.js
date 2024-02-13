#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const updatedNum = number + 1;
  theFunction(updatedNum);
};
