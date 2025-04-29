# O(nlogn)
import collections

class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = collections.Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashMap[key] += 1
        maxValue = max(hashMap.values())
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count

#god mode implementation due to 1 <= n <= 10*4 (10k) 9999
class Solution:
    def countLargestGroup(self, n: int) -> int:
        dp = {0: 0}
        counts = [0] * (4 * 9)
        for i in range(1, n + 1):
            quotient, reminder = divmod(i, 10)
            dp[i] = reminder + dp[quotient]
            counts[dp[i] - 1] += 1

        return counts.count(max(counts))


# Index out of bounds but passes a few tests
class Solution:
    def countLargestGroup(self, n: int) -> int:
        numbers = []
        counter = []

        for i in range(1, n+1):
            if i < 10: 
                numbers.append([i])
                counter.append(1)
            elif i>= 10:
                k = i
                sum = 0
                for j in range(len(str(i))-1):
                    # Sum did not reiterate to be < 10
                    sum += k%10
                    k //= 10
                    if sum >= 10:
                        sum = sum%10 + sum//10
                    if k < 10: break
                numbers[sum].append(i)
                counter[sum] += 1

        return counter.count(len(max(numbers, key=len)))