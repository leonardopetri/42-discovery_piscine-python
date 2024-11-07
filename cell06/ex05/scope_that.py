#!/usr/bin/env python3

def add_one(value: int):
    value += 1

value_to_add: int = 10

print(value_to_add)
add_one(value_to_add)
print(value_to_add)

#o valor impresso é o mesmo pois a passagem de parametros para o método é por valor e não referencia.