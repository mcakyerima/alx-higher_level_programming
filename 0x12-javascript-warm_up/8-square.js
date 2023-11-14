#!/usr/bin/node

const repeat = parseInt(process.argv[2], 10);
if (!isNaN(repeat)) {
  for (let i = 0; i < repeat; i += 1) {
    console.log('X'.repeat(repeat));
  }
} else {
    console.log('Missing size');
}
