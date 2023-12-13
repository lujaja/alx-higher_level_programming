#!/usr/bin/node
let x = process.argv[2];
x = parseInt(x, 10);
if (!x) { console.log('Missing number of occurrences'); } else { for (; x > 0; x--) { console.log('C is fun'); } }
