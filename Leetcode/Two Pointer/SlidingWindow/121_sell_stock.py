# First attempt (didnt make it) was O(nlogn) cause my right pointer would just iterate mindlessly
# Actual solution explained by Neetcode. 

# Sol 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy low, sell high
        # Which means in the sliding window, we set left to the lowest possbile then right iterates through
        l, r = 0, 1  #left = buy, right = sell
        high = 0

        while r < len(prices):
            if prices[l] < prices [r]:
                curr = prices[r] - prices[l]
                high = max(high, curr)
            else:
                l = r
            r += 1
        return high


# Iterate through remainder of array, if diff > maxp, maxp = diff -- diff < 0, buyval = sellval
# Same logic as sol 1 but less readable, faster cause overlapped assignment, cost more memory since it initializes a loop
# Sol 2   
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        buyVal = prices[0]
        for sellVal in prices[1:]:
            diff = sellVal - buyVal
            if diff > maxp:
                maxp = diff
            if diff < 0:
                buyVal = sellVal
        return maxp      
