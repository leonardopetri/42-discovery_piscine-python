#!/usr/bin/env python3

import sys
from re import match

if len(sys.argv[1:]) == 0:
    quit()

#SEM MATCH
# for parameter in sys.argv:
#     endsWithIsm: str = parameter.upper()[len(parameter) - 3:] == "ISM"

#     if not (endsWithIsm):
#         print(parameter)


#COM MATCH, COMO SUGERIDO
for arg in sys.argv[1:]:
    if not (match(r"^.*ISM$", arg.upper())):
        print(arg)