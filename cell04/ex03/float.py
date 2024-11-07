#!/usr/bin/env python3

number = float(input('Give me a number: '))

isInt = number - int(number) == 0

if isInt:
    print('This number is an integer.')
else:
    print('This number is a decimal.')