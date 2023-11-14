#!/usr/bin/node

const inputNumbers = process.argv.slice(2);
function findSecondLargest (array) {
  if (array.length < 2  || array.some(isNaN)) {
    return (0);
  }
  const sortedArray = array.map(Number).sort((a, b) => a - b);  return (sortedArray[sortedArray.length -2]);
}
console.log(findSecondLargest(inputNumbers));
