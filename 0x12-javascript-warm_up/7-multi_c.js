#!/usr/bin/node
const myVar = process.argv;
let n;
if (!isNaN(myVar[2])) {
  n = parseInt(myVar[2]);
  while (n !== 0) {
    console.log('C is fun');
    n = n - 1;
  }
} else {
  console.log('Missing number of occurrences');
}
