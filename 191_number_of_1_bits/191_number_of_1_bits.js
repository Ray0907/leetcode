/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {
  let count = 0;
  // while (n) {
  //     count += n & 1; // Check the least significant bit
  //     // >>>= is known as the unsigned right shift assignment bitwise operator.
  //     n >>>= 1; // Shift right to check the next bit
  // }
  // Brian Kernighan algorithm
  while (n) {
    n &= n - 1;
    count += 1;
  }

  return count;
};
