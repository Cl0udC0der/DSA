# Best solution, same shit but made use of mapping immediately instead of case
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack


# My final solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            match i:
                case "(" | "[" | "{":
                    stack.append(i)
                case ")" | "]" | "}":
                    if len(stack) == 0: return False
                    lastElem = stack.pop()
                    if i != pairs[lastElem]:
                        return False
        if len(stack) > 0: return False
        return True


# Naive solution for base case same parenthesis type (AKA () )
class Solution:
    def isValid(self, s: str) -> bool:
        counter = 0
        for i in s:
            match i:
                case "(" | "[" | "{":
                    counter += 1
                case ")" | "]" | "}":
                    counter -= 1
            print(counter)
            if counter < 0:
                return False
        if counter > 0:
            return False
        else:
            return True
