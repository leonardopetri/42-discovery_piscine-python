#!/usr/bin/env python3

number_str: str = input('Enter a number less than 25\n')

if not number_str.isnumeric():
    print('Error')
    quit()

number = int(number_str)

if number > 25:
    print('Error')
else:
    while number <= 25:
        print('Inside the loop, my variable is', number)
        number += 1