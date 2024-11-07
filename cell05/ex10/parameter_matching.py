#!/usr/bin/env python3

import sys

if len(sys.argv[1:]) != 1:
    print('none')
    quit()

parameter: str = input("What was the parameter? ")

if sys.argv[1] == parameter:
    print("Good job!")
else:
    print("Nope, sorry...")
