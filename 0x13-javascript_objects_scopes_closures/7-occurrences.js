#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  list.forEach(function (val) {
    if (val === searchElement) {
      occ++;
    }
  });
  return occ;
};
