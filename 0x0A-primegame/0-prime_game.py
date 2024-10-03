#!/usr/bin/python3

"""
This module provides functions to determine the winner of a prime game.

Functions:
  isWinner(x, nums):"""


def getPrimes(n):
    """
    Get all prime numbers less than or equal to a given number.

    Args:
      n (int): The upper limit (inclusive) to find prime numbers.

    Returns:
      list: A list of prime numbers less than or equal to n.
    """
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
    """
    Determines the winner of the prime game.

    The game is played as follows:
    - Maria and Ben take turns picking prime numbers from a list of numbers from 1 to n.
    - The player who cannot pick a prime number loses the game.
    - The winner is determined by the number of rounds won by each player.

    Args:
      x (int): The number of rounds.
      nums (list): A list of integers representing the upper limit of numbers for each round.

    Returns:
      str: The name of the player with the most wins ("Maria" or "Ben").
         If the number of rounds is invalid or the input list is empty, returns None.
    """
    # if x < 1 or not nums:
    #     return None
    if x != len(nums):
        return None

    Maria = 0
    Ben = 0

    for n in nums:
        if (n < 1 or n > 10000):
            # print("here")
            continue
        primes = getPrimes(n)
        # print(primes)

        if len(primes) % 2 == 0:
            Ben += 1
            # print("Ben")
        else:
            Maria += 1
            # print("Maria")
    if Maria > Ben:
        return "Maria"
    return "Ben"
