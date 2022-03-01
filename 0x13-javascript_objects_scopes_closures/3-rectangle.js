#!/usr/bin/node
let o = '';
let m;
let n;
class Rectangle {
  print () {
    n = this.height;
    while (n !== 0) {
      m = this.width;
      while (m !== 0) {
        o = o + 'X';
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

  constructor (w, h) {
    if (w <= 0 || h <= 0 || h === undefined || w === undefined) {
      Object.create(Rectangle);
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
