#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.endsWith('/18/')) {
        count++;
        break;
      }
    }
  }
  console.log(count);
});
