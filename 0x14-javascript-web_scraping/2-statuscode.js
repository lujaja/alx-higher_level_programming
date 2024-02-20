#!/usr/bin/node
/**
 * Display ststus code of a url request
 */

const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
