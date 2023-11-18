/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
  n = matrix.length;

  for (i = 0; i < n; i++) {
    for (j = i; j < n; j++) {
      let temp = matrix[i][j];
      matrix[i][j] = matrix[j][i];
      matrix[j][i] = temp;
    }
  }
  for (i = 0; i < n; i++) {
    matrix[i].reverse();
  }
  return matrix;
};
