#!/usr/bin/python3
"""Prime Game"""


def getPrimes(n):
    """Get all prime numbers less than n"""
    primes = []
    for i in range(2, n + 1):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return primes


def isWinner(x, nums):
    """Prime Game"""
    Maria = 0
    Ben = 0
    for n in nums:
        primes = getPrimes(n)
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    return "Ben"
