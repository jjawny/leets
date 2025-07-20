/**
 * BIG-O: O(n) using GREEDY, O(n^2) using basic loops
 *  Solution w thoughts 💭
 *  #easy #greedy
 */
function maxProfit(prices: number[]): number {
  // ------------ BASIC SOLUTION ------------
  // O(n^2/2) = O(n^2) Save the max diff for each pair of days
  // const profitsSet = new Set<number>();
  // for (let i = 0; i < prices.length; i++) {
  //     let maxProfitForDay = 0;
  //     const buy = prices[i];
  //     for (let j = i + 1; j < prices.length; j++) {
  //         const sell = prices[j];
  //         const currProfit = sell - buy;
  //         if (currProfit > maxProfitForDay) {
  //             maxProfitForDay = currProfit;
  //         }
  //     }
  //     profitsSet.add(maxProfitForDay);
  // }

  // O(n) return the max
  // let res = 0;
  // for (const profit of profitsSet) {
  //     if (profit > res) res = profit;
  // }
  // return res;

  // ------------ GREEDY TIME ------------
  // The basic solution works (passes tests)
  //  but doesn't scale for large number of prices (fails submission)
  // The greedy approach will save the max profit based on the curr price and the most min price seen
  // From O(n^2) to O(n)
  let minPrice = Infinity;
  let maxProfit = 0;
  for (let price of prices) {
    const isSmallerPriceToBuyAt = price < minPrice;
    if (isSmallerPriceToBuyAt) minPrice = price;
    else maxProfit = Math.max(maxProfit, price - minPrice);
  }
  return maxProfit;
}
