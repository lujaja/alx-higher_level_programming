#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
(!a || !b) ? console.log(NaN) : add(a, b);
