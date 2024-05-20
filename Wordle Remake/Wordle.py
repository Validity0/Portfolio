import random
five_letter_words = [
    "apple", "brave", "crisp", "drama", "eagle",
    "flame", "grape", "harsh", "ideal", "jolly",
    "knack", "lemon", "mango", "noble", "ocean",
    "piano", "queen", "roast", "shine", "tiger",
    "unity", "vivid", "waste", "xenon", "yield", 
    "zebra", "charm", "fable", "globe", "hover",
    "inbox", "jazzy", "kudos", "lunar", "marry",
    "neigh", "oasis", "plumb", "quilt", "raven",
    "sheep", "torch", "umbra", "vigor", "whale",
    "xylol", "youth", "zesty", "brisk", "clock",
    "ditch", "elbow", "froze", "glint", "hover",
    "ivory", "jumpy", "kinky", "latch", "mirth",
    "nerdy", "opine", "prism", "quake", "resin",
    "scout", "trove", "ultra", "venom", "wrath",
    "yacht", "zephy"
]

correctWord = "mango"
guess = input("Guess: ")
for letter in range(len(correctWord)):
    if guess[letter] == correctWord[letter]:
        print(guess[letter].upper(), end="")
    elif guess[letter] in correctWord:
        print(guess[letter].lower(), end="")
    else:
        print("-", end="")
