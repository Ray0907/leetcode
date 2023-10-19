/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  let result = 0;

  for (let i = 0; i < 32; i++) {
    // Shift the result to the left to make room for the next bit
    result <<= 1;

    // Use a bitwise OR operation to add the current bit to the result
    result |= n & 1;

    // Right-shift the input number to get the next bit
    n >>= 1;
  }

  return result >>> 0;
};
