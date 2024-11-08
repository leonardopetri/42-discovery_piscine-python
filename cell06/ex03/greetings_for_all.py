#!/usr/bin/env python3

def greetings(name = "noble stranger") -> None:
    if not isinstance(name, str):
        print(f"Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)