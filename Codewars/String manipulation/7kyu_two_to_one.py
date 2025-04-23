def longest(s1, s2):
    #turn both strings to a list, then a set for distinct values, 
    set1 = set(list(s1))
    set2 = set(list(s2))
    dist = list(set1.union(set2))
    dist.sort()
    str1 = ''.join(dist)
    return str1

def longest(s1, s2):
    # your code
    return "".join(sorted(set(s1+s2)))