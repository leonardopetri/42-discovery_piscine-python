#!/usr/bin/env python3

def array_of_names(persons: dict) -> list:
    fullname = []
    for first_name in persons:
        fullname.append(f'{first_name.capitalize()} {persons[first_name].capitalize()}')

    return fullname

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))