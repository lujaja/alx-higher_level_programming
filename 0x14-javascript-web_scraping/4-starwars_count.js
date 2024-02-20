#!/usr/bin/node
/**
 * print the number of movies where the character "Wedge Antilies" is present
 */

const request = require('request');

if (process.argv.length !== 3) {
  console.error(`Usage: ${process.argv[1]} address`);
} else {
  const url = 'https://swapi-api.alx-tools.com/api/films/';
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }
    const data = JSON.parse(body);
    let count = 0;
    data.results.forEach(film => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  });
}
