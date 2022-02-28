#!/usr/bin/node
const myVar = process.argv;
let n;
let m;
let o = '';
if (!isNaN(myVar[2])) {
  n = parseInt(myVar[2]);
  if (n >= 0) {
    while (n !== 0) {
      m = parseInt(myVar[2]);
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
  }
} else {
  console.log('Missing size');
}
