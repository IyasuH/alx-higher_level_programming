#!/usr/bin/node
let myArgs = process.argv;
if (myArgs.length <= 2){
    // since the first element is 'process.exePath'
    // and the second element is the path to javaScript 
    console.log('No argument');
}else{
    console.log('Argument found');
}
