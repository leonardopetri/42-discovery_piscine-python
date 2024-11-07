#!/usr/bin/env python3

def greetings(name = ""):
    if not isinstance(name, str):
        print(f"Error! It was not a name.")
    else:
        print_name = "noble stranger" if name == "" else name
        print(f"Hello, {print_name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)