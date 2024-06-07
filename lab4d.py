#!/usr/bin/env python3
# strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(txt):
    return txt[:5]

def last_seven(txt):
    return txt[-7:]

def middle_number(num):
    num_string = str(num)
    return num_string[1:3]

def first_three_last_three(txt1, txt2):
    return txt1[:3] + txt2[-3:] 

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))






