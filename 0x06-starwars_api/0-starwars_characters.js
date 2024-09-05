#!/usr/bin/node

import request from 'request';

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
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    for (const character of characters) {
      const characterData = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body));
          }
        });
      });

      console.log(characterData.name);
    }
  }
});
