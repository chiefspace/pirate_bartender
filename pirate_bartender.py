#!/usr/bin/env python3

import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def bartender(data):
    """This function collects a pirate's drink preferences into a dictionary"""
    customer_preferences = {}
    for key, value in data.items():
        customer_input = input(value + " ")
        customer_preferences[key] = (customer_input == "y" or customer_input == "yes")

    return customer_preferences


def construct_drink(_preference, _ingredients):
    """This function creates and returns drink based on a pirate's drink preferences"""
    drink = []
    for key, value in _preference.items():
        if value is True:
            drink.append(random.choice(_ingredients[key]))

    return drink

def main():
    print("Hi there, welcome to Davey Jones' Locker Pub, home o ye Black Pearl!")
    p_preferences = bartender(questions)
    print(p_preferences)
    constructed_drink = construct_drink(p_preferences, ingredients)
    print("\n ... Aaannd Here's your drink :")
    print(constructed_drink)


if __name__ == "__main__":
    main()


