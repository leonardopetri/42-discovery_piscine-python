#!/usr/bin/env python3

number_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_number_array = [number + 2 for number in number_array if number > 5]

number_set = set(new_number_array)

print(number_array)

print(number_set)