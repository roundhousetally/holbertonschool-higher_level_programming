#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const elem in list) {
    if (list[elem] === searchElement) {
      i++;
    }
  }
  return i;
};
