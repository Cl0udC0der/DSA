#Solution from Neetcode, hashmap is the way 
# Create hash of value, index then iterate thru nums to find if the difference between current item exists then return both
def twoSum(nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, x in enumerate(nums):
            hashMap[x] = i
        for i, x in enumerate(nums):
            result =  target - x
            if result in hashMap and hashMap[result] != i:
                return [i, hashMap[result]]


print(twoSum([2,4,5,6,7,2], 12))

# I have no memory of this
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}  # Hash table to store number and its index
    for i, num in enumerate(nums):
        complement = target - num  # Find the complement
        if complement in num_map:
            return [num_map[complement], i]  # Return indices of complement and current number
        num_map[num] = i  # Store the number with its index
