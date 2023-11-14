#!/usr/bin/node

/**
 * Executes the given function a specified number of times.
 * @param {number} count - The number of times to execute the function.
 * @param {Function} callback - The function to be executed.
 */
exports.callMeMoby = function (count, callback) {
  for (let i = 0; i < count; i++) {
    callback();
  }
};

// Example Usage:
// const { callMeMoby } = require('./yourModuleName');
// callMeMoby(5, () => {
//   console.log('Hello, Moby!');
// });
