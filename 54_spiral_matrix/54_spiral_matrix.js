/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  const result = [];

  while (matrix.length > 0) {
    result.push(...matrix.shift());

    if (matrix.length > 0 && matrix[0].length > 0) {
      for (let row of matrix) {
        result.push(row.pop());
      }
    }
    if (matrix.length > 0) {
      let row = matrix.pop();
      result.push(...row.reverse());
    }

    if (matrix.length > 0 && matrix[0].length > 0) {
      for (let i = matrix.length - 1; i >= 0; i--) {
        result.push(matrix[i].shift());
      }
    }
  }
  return result;
};
