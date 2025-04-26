
# Learned about setting defaultdict(type). Absolute game changer. After that I saw
# how another user just put in the values themselves instead of the index (which I did)
# Also ''.join(not_a_string) is apparently the fastest way to do things
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        my_dict = defaultdict(list)

        for x in strs:
            arrange = ''.join(sorted(x))
            my_dict[arrange].append(x)

        return list(my_dict.values())