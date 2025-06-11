# Basically we have 3 pointers, one for the lower bound, then the higher bound, then the closest result to the answer
# To get the square root of a number, we we check the difference between the floor division of high - low
# If the difference^2 is greater than n, high is set to the difference, else it is set to low
# repeat until low <= high

class Solution:
    def mySqrt(self, x: int) -> int:
        high = x
        low = 1
        result = 0

        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid <= x:
                result = mid
                low = mid + 1
            
            else:
                high = mid - 1

        return result

