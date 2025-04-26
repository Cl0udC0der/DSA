#We can use edge cases and constraints to cut out execution time by a bit. Beast mode solution
# cut out a bunch of samples short by measuring len instead of going through the whole execution

# Beast mode 4ms solution. Goes through each character and compares if the occurence matches its counterpart
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for i in set(t):
            if s.count(i)!=t.count(i):
                return False
        return True


#First solution, naive? bottom of the list at 20ms
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if (sorted(s) == sorted(t)): return True
        return False