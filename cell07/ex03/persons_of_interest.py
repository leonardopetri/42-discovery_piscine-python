#!/usr/bin/env python3

def famous_births(historical_figures: dict):
    historical_figures_values = list(historical_figures.values())
    sorted_figures = sorted(historical_figures_values, key=lambda x: int(x["date_of_birth"]))
    for figures in sorted_figures:
        print(f'{figures["name"]} is a great scientist born in {figures["date_of_birth"]}')

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)