#!/usr/bin/node

import request from 'request';

const url = 'https://swapi-api.alx-tools.com/api/films';
const movieId = process.argv[2];

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
