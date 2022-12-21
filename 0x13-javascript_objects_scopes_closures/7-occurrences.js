#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (const num of list) {
    if (num === searchElement) {
      c += 1;
    }
  }
  return (c);
};
