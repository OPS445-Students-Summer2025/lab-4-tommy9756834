#!/usr/bin/env python3
# Author ID: [seneca_id]

def is_digits(sobj):
    for i in sobj:
        if i in "1234567890":
            pass
        else:
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')