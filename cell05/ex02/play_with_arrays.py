#!/usr/bin/env python3

number_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_number_array = [number + 2 for number in number_array if number > 5]

print(f'Original array: {number_array}')

print(f'New array: {new_number_array}')
