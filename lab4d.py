#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(str):
    return str[:5]
def last_seven(str):
    return str[-7:]

def middle_number(integer):
    string = str(integer)
    return string[1:3]

def first_three_last_three(arg1, arg2):
    string = arg1[:3]+arg2[-3:]
    return str(string)
    


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))