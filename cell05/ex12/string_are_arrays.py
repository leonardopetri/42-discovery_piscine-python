#!/usr/bin/env python3

import sys

if len(sys.argv[1:]) != 1:
    print('none')
    quit()

count: str = ''
for letter in sys.argv[1]:
    if letter == 'z':
        count += 'z'

print('none' if len(count) == 0 else count)