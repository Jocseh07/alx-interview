#!/usr/bin/python3
"""Prime Game"""


def sieve(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes"""
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p]):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def isWinner(x, nums):
    """Prime Game"""
    if x != len(nums):
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    Maria = 0
    Ben = 0

    for n in nums:
        current_primes = [p for p in primes if p <= n]
        if len(current_primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
