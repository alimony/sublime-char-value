# encoding: utf-8

'''This function lives in a separate file so it can be tested by tests.py'''


def char_value(s):
    output = ''

    for char in s:
        # Put a space between each char value.
        output += '%s ' % str(ord(char))

    # Remove any trailing whitespace, meaning no spaces if single char.
    output = output.rstrip()

    return output
