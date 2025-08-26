#  sum all below num n that are Multiples of 3 or 5
# If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.
# Find the sum of all the multiples of $3$ or $5$ below $1000$.


# Will hit recursion depth cap on larger numbers. Also doesnt work if asked for <n instead of =n
def solution1(n):
    if n == 0:
        return 0
    if n % 3 == 0 or n % 5 == 0:
        return n + solution1(n - 1)
    else:
        return solution1(n - 1)

# One liner that more or less does the same  
def solution2(n):
    total_sum = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
    return total_sum

print(solution2(1000))
