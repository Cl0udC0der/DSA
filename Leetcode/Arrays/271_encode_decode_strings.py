# Neetcode Optimal
# 
class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res


# Incredibly naive solution which will work for many cases but fail on majority of edge cases. 
class Solution:

    def encode(self, strs: List[str]) -> str:
        return "#".join(strs)

    def decode(self, s: str) -> List[str]:
        out = []
        word = ""
        for i in s:
            if (i == "#"):
                out.append(word)
                word = ""
            else :
                word += i
        out.append(word)
        return out