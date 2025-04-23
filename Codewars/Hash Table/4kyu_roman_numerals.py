class RomanNumerals:
    def from_roman(s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
                 'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in roman:
                num+=roman[s[i:i+2]]
                i+=2
            else:
                #print(i)
                num+=roman[s[i]]
                i+=1
        return num
    
    def to_roman(num):
        roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        romnum = ''
        
        for (n, rom) in roman:
            (d, num) = divmod(num, n)
            romnum += rom * d
            
        return romnum

class RomanNumerals:

    def to_roman(val):
        onesRoman = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tensRoman = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hundsRoman = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thousRoman = ["","M","MM","MMM","MMMM"]
            
        ones =  onesRoman[val % 10]
        tens = tensRoman[val // 10 % 10]
        hunds = hundsRoman[val // 100 % 10]
        thous = thousRoman[val // 1000]
        
            
        return thous + hunds + tens + ones

    def from_roman(roman_num):
        out = 0 
        mx = 0
        for cur in map(lambda c: { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 } [c], roman_num[::-1]):
            if cur >= mx: 
                out += cur
                mx = cur
            else:
                out -= cur
        
        return out