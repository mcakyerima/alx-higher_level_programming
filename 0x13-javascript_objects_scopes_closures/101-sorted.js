#!/usr/bin/node
const { dict } = require('./101-data');

const reversedDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (!reversedDict[occurrences]) {
    reversedDict[occurrences] = [userId];
  } else {
    reversedDict[occurrences].push(userId);
  }
}

console.log(reversedDict);
