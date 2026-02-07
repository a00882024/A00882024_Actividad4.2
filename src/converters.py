"""Number conversion functions implementation."""


def decimal_to_binary(number):
    """
    Convert a decimal number to binary string.

    Division by 2 algorithm

    1. Divide number by 2
    2. Record the remainder [0, 1]
    3. Repeat with the quotient until reaching 0
    4. Concatenate the remainders in reverse order

    7 / 2 = 3 rem 1
    3 / 2 = 1 rem 1
    1 / 2 = 0 rem 1
    """
    if number == 0:
        return '0'

    result = ''

    n = abs(number)

    while n > 0:
        # We use modulo to get the remainder
        remainder = n % 2
        # Need to turn to strings otherwise it might try arithmetic addition
        result = str(remainder) + result
        # Divide by 2 and ensure int result
        n = int(n/2)

    # if negative we put a minus sign at the beginning
    if number < 0:
        result = '-' + result

    # Return the built out binary base value as a string
    return result


def decimal_to_hexadecimal(number):
    """
    Convert a decimal number to hexadecimal string.

    We use a similar algorithm but divide by 16 and map
    the remainders to a digit between 0-9 and A-F


    A -> 10
    B -> 11
    C -> 12
    D -> 13
    E -> 14
    F -> 15

    173 / 16 = 10 remainder 13 -> D
    """
    # No need to process if the value is already 0
    if number == 0:
        return '0'

    # We'll use this to find the correct digit
    hex_digits = '0123456789ABCDEF'
    result = ''

    n = abs(number)

    while n > 0:
        # Find the remainder
        remainder = n % 16
        # Prepend the digit left of the current result
        result = hex_digits[remainder] + result
        # Find the integer result of divinding the number by 16
        n = int(n / 16)

    # If negative let's prepend a minus sign
    if number < 0:
        result = '-' + result

    return result
