#!/usr/bin/python3
""" Code to validate UTF-8 Encoding
"""


def validUTF8(data):
    """FUnction to validate The list of bytes

    Args:
        data: Used for tracking the number of arguments in
        a list
    Returns:
        To return a  valid UTF-8 code
    """
    num_in_bytes = 0

    num1 = 1 << 7  # This is for 128 bit tracking 10000000
    num2 = 1 << 6  # This is for 64 bit tracking  01000000

    for nums in data:
        byte = nums & 0xff  # This is to get the least Significant bit

        if num_in_bytes == 0:
            if (byte & num1) == 0:
                # This is for one byte character
                continue

            elif (byte & num1) and (byte & num2):
                num = num1
                print("before while", num)
                while (byte & num):
                    num_in_bytes += 1
                    num >>= 1

                # Making sure UTF-8 is not more than 4 bytes
                if num_in_bytes == 1 or num_in_bytes > 4:
                    print("before false", num_in_bytes)
                    return False
            else:
                return False
        else:
            if not (byte & num1 and not (byte & num2)):
                return False

        num_in_bytes -= 1
        print(num_in_bytes)

    return num_in_bytes == 0  # To return True if all bytes matched pattern
