#!/usr/bin/node
const myVar = 'My number: ';
const arg = parseInt(process.argv[2], 10);
if (!arg) { console.log('Not a number'); } else { console.log(myVar + arg); }
