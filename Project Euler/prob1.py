# Multiples of 3 or 5, sum all below num n

# Will hit recursion depth cap on larger numbers. Also doesnt work if asked for <n instead of =n
def solution1(n):
    if n == 0:
        return 0
    if n % 3 == 0 or n % 5 == 0:
        return n + solution1(n - 1)
    else:
        return solution1(n - 1)



def solution2(n):
    total_sum = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)