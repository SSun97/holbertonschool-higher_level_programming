#!/usr/bin/node
// counts number of occurences of element in list
exports.nbOccurences = function (list, element) {
  const n = list.filter(x => x === element).length;
  return n;
};
