import string

def find_missing_letter(chars):
    ab = []
    cap = chars[0].isupper()
    if cap:
        ab = string.ascii_uppercase
    else:
        ab = string.ascii_lowercase
    start = ab.index(chars[0])
    for x in chars:
        start += 1
        if not(ab[start] in chars):
            return ab[start]
    return ab[start]

def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

def find_missing_letter(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start+i]:
            return alphabet[start+i]
        

#Reduce to ascii