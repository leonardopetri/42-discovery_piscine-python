#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")
    quit()

base_number: int = 0
while base_number <= 10:
    result_string: str = ""

    multiplier: int = 0 
    while multiplier <= 10:
        result_string += f' {base_number*multiplier}'
        multiplier += 1
    
    print(f"Table de {base_number}:{result_string}")
    base_number += 1