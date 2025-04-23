def DNA_strand(dna):
    ans = ''
    for x in dna:
        if x == 'A': ans += 'T'
        elif x == 'T': ans += 'A'
        elif x == 'G': ans += 'C'
        elif x == 'C': ans += 'G'
    return ans

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])