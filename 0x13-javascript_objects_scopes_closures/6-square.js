#!/usr/bin/node
const Square5 = require('./5-square');
let o = '';
let m;
let n;
class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    n = this.height;
    while (n !== 0) {
      m = this.width;
      while (m !== 0) {
        o = o + c;
        m = m - 1;
      }
      if (n > 1) {
        o = o + '\n';
      }
      n = n - 1;
    }
    console.log(o);
    o = '';
  }
}
module.exports = Square;
