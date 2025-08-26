import math
import time
from typing import Optional

# ⚠️⚠️⭕ I actually legit dont understand this problem, return at a later date⭕⚠️⚠️
def largestPrimeFactor(n):
    # Geeks for geeks solution
    largestPrime = -1

    # Check for factors of 2
    while n % 2 == 0:
        largestPrime = 2
        n //= 2

    # Check for odd factors starting from 3
    i = 3
    while i * i <= n:
        while n % i == 0:
            largestPrime = i
            n //= i
        i += 2

    # If n is still greater than 2, it is
    # a prime number
    if n > 2:
        largestPrime = n

    return largestPrime


if __name__ == "__main__":
    n = 15
    res = largestPrimeFactor(n)
    print(res)

def highest_prime_factor_optimized(n: int) -> Optional[int]:
    """
    Claude optimized highest prime
    More optimized version using wheel factorization principles.
    Skips multiples of 2 and 3 for better performance.
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return None
    
    highest_prime = None
    
    # Handle factors 2 and 3
    while n % 2 == 0:
        highest_prime = 2
        n //= 2
    
    while n % 3 == 0:
        highest_prime = 3
        n //= 3
    
    # Check factors of form 6k±1 up to √n
    factor = 5
    while factor * factor <= n:
        # Check 6k-1 and 6k+1
        for candidate in [factor, factor + 2]:
            while n % candidate == 0:
                highest_prime = candidate
                n //= candidate
        factor += 6
    
    # If n is still greater than 1, then it's a prime factor
    if n > 1:
        highest_prime = n
    
    return highest_prime


if __name__=='__main__':
    n = 600851475143
    print(highest_prime_factor_optimized(n))