#!/usr/bin/env python3

import sys

def downcase_it(string_to_downcase: str) -> str:
    return string_to_downcase.lower()

if len(sys.argv[1:]) == 0:
    print('none')
    quit()

for i in sys.argv[1:]:
    print(downcase_it(i))