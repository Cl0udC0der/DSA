# There was a comment under a solution that read: "how tf does some arrive at this ? how many years of solving does it take ?"
# I agree



# Neetcode explanation about going by each element and checking if there is a left neighbor to determine start, and right neighbor (while incrementing) to determine
# sequence continuation was good, his implementation went overtime due to the new test cases
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet  = set(nums)
        longest = 0

        for n in nums:
            #check if start of sequence
            if (n-1) not in numSet :
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


# This solution was the most common. Exactly the same exact 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums)
        longest=0
        for num in s:
            if num - 1 not in s:
                curr = num
                currsteak = 1
                while curr+1 in s:
                    curr+=1
                    currsteak+=1

                longest = max(longest, currsteak)
        
        return longest
    
# My initial solution, it was cooked the moment I used .sort()
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = 1
        result = 1
        nums.sort()
        print(nums)
        if len(nums) == 0: return 0
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                curr += 1
                print(nums[i], nums[i+1], curr)
            elif nums[i] == nums[i+1]:
                continue
            else:
                result = max(result, curr)
                curr = 1
                print("res: ", result)
        result = max(result, curr)

        return result