#!/usr/bin/python3
"""Prime Game"""


def getPrimes(n):
    """Get all prime numbers less than n"""
    primes = []
    for i in range(2, n + 1):
        isPrime = True
        for j in primes:
            # for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return primes


def isWinner(x, nums):
    """Prime Game"""
    if x < 1 or not nums:
        return None
    if x != len(nums):
        return None
    Maria = 0
    Ben = 0
    rounds = 0
    for n in nums:
        # if rounds == x:
        #     break
        # round += 1
        primes = getPrimes(n)
        if len(primes) % 2 == 0:
            Ben += 1
            print("Ben")
        else:
            Maria += 1
            print("Maria")
    if Maria > Ben:
        return "Maria"
    return "Ben"
