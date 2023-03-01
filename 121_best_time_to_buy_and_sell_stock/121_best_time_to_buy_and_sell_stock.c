/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let results = 0
    let lowest = prices[0];

    for(let price of prices) {
       lowest = price > lowest? lowest : price
       results = results > price - lowest ? results: price - lowest 
    }
    return results
};
