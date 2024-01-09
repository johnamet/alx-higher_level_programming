#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  let updatedNum = number + 1;
  theFunction(updatedNum);
}
