#!/usr/bin/node
/**
 * Display ststus code of a url request
 */

const request = require('request');
const movieId = process.argv[2];

if (process.argv.length !== 3) {
  console.error(`Usage: ${process.argv[1]} movieId`);
} else {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error.message);
      return;
    }
    const title = JSON.parse(body).title;
    console.log(title);
  });
}
