#!/usr/bin/node
const arg = process.argv.slice(2);
if (!arg.length) {
  console.log('No argument');
} else if (arg.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
