# 2 part approach. 1 pass to go up to the array and create the prefix which is stored in the output to save memory
# Next pass is in reverse and uses the output and logic of prefix in conjunction with postfix to get the resulting 
# products to arrive at the proper solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
