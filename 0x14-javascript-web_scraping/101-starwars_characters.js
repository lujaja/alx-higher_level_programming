#!/usr/bin/node
/**
 * Prints all characters of starwars
 */
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
let names;
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  data.characters.forEach(link => {
    request(link, (err, response, body) => {
      if (err) {
        console.log(err);
      }
      names = JSON.parse(body);
      console.log(names.name);
    });
  });
});
