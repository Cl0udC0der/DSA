def digital_root(n):
    ans = 0
    for x in str(n):
        ans += int(x)
    if ans >= 10: return digital_root(ans)
    return ans

def digital_root(n):
    print(n)
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root1(n):
	return n%9 or n and 9 

def digital_root(n):
    # ...
    while n>9:
        n=sum(map(int,str(n)))
    return n
