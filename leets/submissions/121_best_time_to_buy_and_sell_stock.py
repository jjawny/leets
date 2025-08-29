from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ================= BRUTE FORCE ===================
        # ##brute-force
        # TIME: Always O(n^2)
        # SPACE: Always O(1) using counters only
        # PSEUDO CODE:
        #   Outter loop, where each item is the buy
        #       Inner loop, where each item is the sell (starting from day after buy day)
        #           Saves the largest sell
        #       Repeat outter loop only if buy is lower than the smallest previous buy
        # min_buy, max_profit = None, 0 # Use None >>> 0 for initial min_buy as prices can be negatives
        # for buy_idx, buy in enumerate(prices):
        #     if min_buy and buy >= min_buy:
        #         continue
        #     min_buy = buy
        #     for sell_idx in range(buy_idx + 1, len(prices)):
        #         sell = prices[sell_idx]
        #         profit = sell - buy
        #         max_profit = max(profit, max_profit)
        # return max_profit
        # ================= TWO POINTERS ===================
        # ##two-pointers ##sliding-windows
        # TIME: Always O(n)
        # SPACE: Always O(1) using counters only
        # PSEUDO CODE:
        #   Buy starts on day 1, sell starts on day 2
        #   1x loop, where each item is the sell
        #       If the sell is larger than the buy, we need to check if the profit is also larger (save!)
        #       If the sell is smaller, we found a better buy day (save!)
        # left, right = 0, 1
        # max_profit = 0
        # while right < len(prices):
        #     buy, sell = prices[left], prices[right]
        #     if sell > buy:
        #         profit = sell - buy
        #         max_profit = max(max_profit, profit)
        #     else:
        #         left = right
        #     right += 1
        # return max_profit
        # ================= GREEDY ===================
        # ##greedy
        # TIME: Always O(n)
        # SPACE: Always O(1) using counters only
        # PSEUDO CODE:
        #   Basically the same as the two-pointers, but one-pointer + simpler mental model (no sliding window)
        min_buy, max_profit = None, 0 # Use None >>> 0 for initial min_buy as prices can be negatives
        for price in prices:
            if min_buy is None:
                min_buy = price
                continue
            is_cheaper_day_to_buy = price < min_buy
            if is_cheaper_day_to_buy:
                min_buy = price
            else:
                profit = price - min_buy
                max_profit = max(max_profit, profit)
        return max_profit
