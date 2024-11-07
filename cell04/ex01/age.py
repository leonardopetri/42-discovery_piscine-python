#!/usr/bin/env python3

age: int = int(input('Please tell me your age: '))

print(f'You are currently {age} years old.')

count: int = 1
while count <= 3:
    print(f"In {count*10} years, you'll be {age+(count*10)} years old.")
    count += 1