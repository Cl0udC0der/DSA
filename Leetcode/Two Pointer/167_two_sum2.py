# Pointer Solution
class Solution(object):
    def twoSum(self, numbers, target):    
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1


# Hashmap Solution based on earlier two sum
class Solution(object):
    def twoSum(self, numbers, target):  
        hashMap = {}
        for i, x in enumerate(numbers):
            hashMap[x] = i
        for i, x in enumerate(numbers):
            result =  target - x
            if result in hashMap and hashMap[result] != i:
                return [i+1, hashMap[result]+1]