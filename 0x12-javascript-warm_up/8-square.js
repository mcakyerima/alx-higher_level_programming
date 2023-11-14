#!/usr/bin/node

repeat = parseInt(process.argv[2], 10);
if (!isNaN(repeat)) {
  for (let i = 0; i < repeat; i++) {
    console.log('X'.repeat(repeat));
  }
} else {
    console.log('Missing size');
}
