#!/usr/bin/env python3

first_number = int(input('Enter the first number:\n'))
second_number = int(input('Enter the second number:\n'))

multiplied = first_number*second_number

print(f'{first_number} x {second_number} = {multiplied}')

if multiplied < 0:
    print('The result is negative.')
elif multiplied > 0:
    print('The result is positive.')
else:
    print('The result is both positive and negative.')