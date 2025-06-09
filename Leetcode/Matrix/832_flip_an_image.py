# The problem I faced in the IBM frontend  problem. I didn't understand how to flip and it was this easy.
# 0 ms, not much extra memory since it uses the input
# Basically for every row in the 2d array, use reverse() and then bitwise XOR on each item on the equivalent column to negate the binary value
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
            for k, j  in enumerate(i):
                i[k] ^= 1
        return image