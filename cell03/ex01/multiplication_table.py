#!/usr/bin/env python3

number: int = int(input("Enter a number\n"))
counter: int = 0

while counter < 10:
    print(f'{counter} x {number} = {counter*number}')
    counter += 1