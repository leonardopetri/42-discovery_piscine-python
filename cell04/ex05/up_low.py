#!/usr/bin/env python3

string_value: str = input('')
aux = ''

for i in string_value:
    aux += i.swapcase()

print(aux)
