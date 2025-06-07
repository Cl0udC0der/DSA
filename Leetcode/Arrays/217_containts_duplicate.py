#Initial implementation, just break it with the set() conversion
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)): return True
        return False
    
# ALternative solution, hash map that increases value for every duplicate. If any value > 1, there are dupes