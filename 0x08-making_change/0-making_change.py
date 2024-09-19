#!/usr/bin/python3
"""
make change for a given amount of money
"""


def makeChange(coins, total):
    """Make change"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    result = 0
    for coin in coins:
        if total <= 0:
            break
        result += total // coin
        total = total % coin
    if total != 0:
        return -1
    return result
