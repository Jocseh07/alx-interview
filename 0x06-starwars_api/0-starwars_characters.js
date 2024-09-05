#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}
const movieId = process.argv[2];
if (movieId < 1 || movieId > 7) {
  console.log('Movie id must be between 1 and 7');
  process.exit(1);
}

const movieUrl = `${url}/${movieId}`;

request(movieUrl, async (error, response, body) => {
  if (error) throw error;
  const movieCharacters = JSON.parse(body).characters;
  getCharacterNames(movieCharacters, 0);
});

function getCharacterNames(movieCharacters, index) {
  if (index === movieCharacters.length) return;
  request(movieCharacters[index], (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    getCharacterNames(movieCharacters, index + 1);
  });
}
