#!/usr/bin/env python3


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


def bartender(strong, salty, bitter, sweet, fruity):
    strong_pref = strong
    salty_pref = salty
    bitter_pref = bitter
    sweet_pref = sweet
    fruity_pref = fruity
    print(fruity_pref)
    
    

print("Hi there, welcome to the Pirate Bartender program")
bartender(**questions)

