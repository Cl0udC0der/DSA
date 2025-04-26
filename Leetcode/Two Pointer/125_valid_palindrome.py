# Reverse string solution
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Filter the string to include only alphanumeric characters and convert to lowercase
        filtered_str = ''.join(c.lower() for c in s if c.isalnum())
        
        # Check if the filtered string is the same as its reverse
        return filtered_str == filtered_str[::-1]

# Initial solution
class Solution(object):
    def isPalindrome(self, s):
        p = list(lower(filter(str.isalnum, str(s))))

        for x in p:
            if x == p[-1]: p.pop()
            else: return False
        return True