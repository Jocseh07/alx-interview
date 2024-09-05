#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films';

request(`${url}/${movieId}`, async (error, response, body) => {
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
