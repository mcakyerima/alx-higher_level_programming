#!/usr/bin/node

const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

const contentSourceFile1 = fs.readFileSync(sourceFilePath1, 'utf8');
const contentSourceFile2 = fs.readFileSync(sourceFilePath2, 'utf8');

fs.writeFileSync(destinationFilePath, contentSourceFile1 + contentSourceFile2);
