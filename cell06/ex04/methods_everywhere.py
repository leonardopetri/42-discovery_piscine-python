#!/usr/bin/env python3

import sys

def shrink(param: str) -> None:
    print(param[slice(8)])

def enlarge(param: str) -> None:
    print(param + "z" * (8 - len(param)))

if len(sys.argv[1:]) == 0:
    print('none')
    quit()

for param in sys.argv[1:]:
    if len(param) > 8:
        shrink(param)
    elif len(param) < 8:
        enlarge(param)
    else:
        print(param)