#!/usr/bin/env python3

import sys

if len(sys.argv[1:]) < 2:
    print('none')
    quit()

for i in sys.argv[::-1]:
    print(i)