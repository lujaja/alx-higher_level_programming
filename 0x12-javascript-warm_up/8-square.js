#!/usr/bin/node
let x = process.argv[2];
x = parseInt(x, 10);
if (!x) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
