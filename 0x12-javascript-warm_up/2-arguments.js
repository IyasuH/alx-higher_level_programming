#!/usr/bin/node
const myArgs = process.argv;
if (myArgs.length <= 2) {
  // since the first element is 'process.exePath'
  // and the second element is the path to javaScript
  console.log('No argument');
} else if (myArgs.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
