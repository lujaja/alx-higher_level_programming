#!/usr/bin/node
/**
 * Thsi script reads and prints the content of a file given as an argument
 */
const fs = require('fs');
const filePath = process.argv[2];

if (process.argv.length < 3) {
  console.log(`Usage: ${process.argv[1]} fileNameToRead`);
  process.exit(1);
} else {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
