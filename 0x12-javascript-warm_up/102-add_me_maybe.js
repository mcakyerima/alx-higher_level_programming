#!/usr/bin/node

/**
 * Adds a given number to itself and passes the result to a callback function.
 * @param {number} number - The number to be added to itself.
 * @param {Function} callback - The callback function to receive the result.
 */
function addMeMaybe(number, callback) {
  const result = number + number;
  callback(result);
}

module.exports.addMeMaybe = addMeMaybe;

// Example Usage:
// const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
// addMeMaybe(4, function (result) {
//   console.log('New value: ' + result);
// });
