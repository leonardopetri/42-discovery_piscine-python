#!/usr/bin/env python3

input_str: str = input("What you gotta say? : ")

while True:
    if input_str == 'STOP':
        break
    input_str = input("I got that! Anything else? : ")