#!/usr/bin/node
const myVar = 'My number: ';
const arg = parseInt(process.argv[2], 10);
!arg ? console.log('Not a number') : console.log(myVar + arg);
