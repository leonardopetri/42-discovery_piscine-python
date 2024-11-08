#!/usr/bin/env python3

import sys
import re

if len(sys.argv[1:]) < 2:
    print('none')
    quit()

count: int = len(re.findall(sys.argv[1], sys.argv[2]))

if count == 0:
    print('none')
    quit()

print(count)