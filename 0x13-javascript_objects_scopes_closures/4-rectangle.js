#!/usr/bin/node
let o = '';
let m;
let n;
class Rectangle {
  print () {
    const x = 'X';
    n = this.height;
    while (n !== 0) {
      m = this.width;
      while (m !== 0) {
        o = o + x;
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

  rotate () {
    n = this.height;
    this.height = this.width;
    this.width = n;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
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
