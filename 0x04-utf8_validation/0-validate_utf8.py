#!/usr/bin/python3


"""
This function checks if a given list of integers represents a
valid UTF-8 encoding.

Parameters:
- data (list): A list of integers representing the UTF-8 encoding.

Returns:
- bool: True if the encoding is valid, False otherwise.
"""


def validUTF8(data):
    # Number of bytes in the current character
    num_bytes = 0

    # Iterate through each integer in the data set
    for num in data:
        # Check if the current byte is a continuation byte
        if num & 0b11000000 == 0b10000000:
            # If it's not a valid continuation byte, return False
            if num_bytes == 0:
                return False
            # Decrement the number of bytes remaining
            num_bytes -= 1
        else:
            # Check the number of bytes in the current character
            if num_bytes > 0:
                return False
            # Determine the number of bytes in the current character
            if num & 0b10000000 == 0:
                num_bytes = 0
            elif num & 0b11100000 == 0b11000000:
                num_bytes = 1
            elif num & 0b11110000 == 0b11100000:
                num_bytes = 2
            elif num & 0b11111000 == 0b11110000:
                num_bytes = 3
            else:
                return False

    # If there are remaining bytes, return False
    if num_bytes > 0:
        return False

    # All checks passed, return True
    return True
