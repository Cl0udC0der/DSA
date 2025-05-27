# Make two pointers, a variable to store current substring, and a variable for the longest thus far
# Iterate from 0 to len(s) adding every unique variable to the array and if there is a duplicate, 
# slowly closing the  window on the left until there is no duplicate, then resume moving other pointer
# Edge cases: empty string, string w blank space
# O(n) time, O(1) space since we're moving along the existing string


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, r -l + 1)
        return longest