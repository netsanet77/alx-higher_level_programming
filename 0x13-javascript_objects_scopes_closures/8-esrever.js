#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  let j = 0;
  const temp = [];
  if (list.length !== 0) {
    while (i < list.length - 1) {
      i++;
    }
    while (i >= 0) {
      temp[j] = list[i];
      i -= 1;
      j += 1;
    }
  }
  return temp;
};
