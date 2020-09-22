#!/usr/bin/node
exports.esrever = function (list) {
  var newlist = [];
  while (list.length) {
    newlist.push(list.pop());
  }
  return newlist;
};
