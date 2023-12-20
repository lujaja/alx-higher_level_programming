#!/usr/bin/node
const arg = process.argv.slice(2);
!arg[0] ? console.log('No argument') : console.log(arg[0]);
