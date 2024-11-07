#!/usr/bin/env python3

import ctypes

def filter_func(member: tuple) -> bool:
    name, hair_color = member
    return hair_color == "red"

def find_the_redheads(family_members: dict) -> ctypes.Array:
    return list(dict(filter(filter_func, family_members.items())).keys())

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(dupont_family))