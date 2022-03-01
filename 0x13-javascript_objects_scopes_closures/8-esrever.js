#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = list.map(list.pop, [...list]);
  return reverse;
};
