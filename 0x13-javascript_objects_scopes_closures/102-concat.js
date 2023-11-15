#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(`Error reading ${sourceFile1}: ${err1.message}`);
    process.exit(1);
  }

  fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(`Error reading ${sourceFile2}: ${err2.message}`);
      process.exit(1);
    }

    const concatenatedData = `${data1}${data2}`;

    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err3) => {
      if (err3) {
        console.error(`Error writing to ${destinationFile}: ${err3.message}`);
        process.exit(1);
      }

      console.log(`${sourceFile1} and ${sourceFile2} have been concatenated to ${destinationFile}`);
    });
  });
});
