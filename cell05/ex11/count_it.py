#!/usr/bin/env python3

import sys

if len(sys.argv[1:]) == 0:
    print('none')
    quit()

print(f"parameters: {len(sys.argv) - 1}")

for i in sys.argv[1:]:
    print(f'{i}: {len(i)}')