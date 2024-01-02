/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let l = 0;
  let r = 1;
  let profit = 0;
  while (r < prices.length) {
    if (prices[r] > prices[l]) {
      profit = Math.max(profit, prices[r] - prices[l]);
    } else l = r;
    r++;
  }
  return profit;
};
