#!/usr/bin/node

import request from 'request';

const url = 'https://swapi-api.alx-tools.com/api/films/';

const characterId = process.argv[2];

// request(url + characterId, (error, response, body) => {
//   if (error) {
//     console.log(error);
//   } else {
//     const characters = JSON.parse(body).characters;
//     const sortedCharacters = characters.sort((a, b) => a - b);
//     console.log(sortedCharacters);
//     for (const character of sortedCharacters) {
//       request(character, (error, response, body) => {
//         if (error) {
//           console.log(error);
//         } else {
//           console.log(JSON.parse(body).name);
//         }
//       });
//     }
//   }
// });

const getMovie = async (url) => {
  request(url, (error, response, body) => {
    if (error) {
      return error;
    } else {
      return JSON.parse(body);
    }
  });
};

console.log(getMovie(url));
