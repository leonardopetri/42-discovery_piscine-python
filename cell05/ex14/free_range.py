#!/usr/bin/env python3

import sys

if len(sys.argv[1:]) != 2:
    print('none')
    quit()

bigger_num: int = int(sys.argv[1]) if int(sys.argv[1]) > int(sys.argv[2]) else int(sys.argv[2])
lower_num: int = int(sys.argv[1]) if int(sys.argv[1]) < int(sys.argv[2]) else int(sys.argv[2])

array = list(range((lower_num), int(bigger_num + 1)))

print(array)