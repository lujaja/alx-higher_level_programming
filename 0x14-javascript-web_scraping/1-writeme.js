#!/usr/bin/node
/**
 * Thsi script reads and prints the content of a file given as an argument
 */
const fs = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];

if (process.argv.length < 3) {
  console.log(`Usage: ${process.argv[1]} filePath stringToWrite`);
  process.exit(1);
} else {
  fs.writeFile(filePath, string, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}
