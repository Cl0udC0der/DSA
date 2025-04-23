#Long if-else approach, high Big(O)
def letters_to_numbers(s):
    total = 0
    # alphabet_dict = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}
    # create it once and then paste the dict
    alphabet_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                'x': 24, 'y': 25, 'z': 26}

    for i in "".join(s.split()):
        if i.isalpha():
            if i.isupper():
                total += 2 * int(alphabet_dict[i.lower()])
            else:
                total += int(alphabet_dict[i])
        elif i.isnumeric():
            total += int(i)
        # else don't add
    return total

#Best case
def letters_to_numbers(sentence):
    result = 0
    
    for char in sentence:
        char_code = ord(char)
        
        # lowercase [a-z]
        if 97 <= char_code <= 122:
            result += (char_code - 96)
        
        # uppercase [a-z]
        if 65 <= char_code <= 90:
            result += (char_code - 64) * 2
        
        # digits
        if 48 <= char_code <= 57:
            result += (char_code - 48)
    
    return result