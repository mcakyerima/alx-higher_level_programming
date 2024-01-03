#!/usr/bin/node

const fs = require('fs');

let fileName = process.argv[2];
let fileContent = process.argv[3];

fs.writeFile(fileName, fileContent, 'utf8', (err) => {
  if (err) {
    cosole.error(err);
  }
});
