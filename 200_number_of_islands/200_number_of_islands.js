/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  let count = 0;

  function dfs(row, col) {
    if (
      0 <= row &&
      row < grid.length &&
      0 <= col &&
      col < grid[0].length &&
      grid[row][col] == "1"
    ) {
      grid[row][col] = "0";

      dfs(row, col - 1);
      dfs(row, col + 1);
      dfs(row - 1, col);
      dfs(row + 1, col);
    }
  }

  for (let row = 0; row < grid.length; row++) {
    for (let col = 0; col < grid[0].length; col++) {
      if (grid[row][col] == "1") {
        dfs(row, col);
        count = count + 1;
      }
    }
  }
  return count;
};
