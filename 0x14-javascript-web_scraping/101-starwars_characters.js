#!/usr/bin/node

const request = require('request');

async function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

async function getMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  return new Promise((resolve, reject) => {
    request.get(url, async (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const movie = JSON.parse(body);
        const characters = movie.characters;

        const characterNames = [];
        for (const characterUrl of characters) {
          const characterName = await getCharacterName(characterUrl);
          characterNames.push(characterName);
        }

        resolve(characterNames);
      }
    });
  });
}

async function main () {
  try {
    const movieId = process.argv[2];
    const characterNames = await getMovieCharacters(movieId);

    for (const characterName of characterNames) {
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
}

main();
