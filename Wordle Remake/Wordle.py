import random
import string
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
    "yacht", "zephy", "slave"
]

alphabet = string.ascii_lowercase
array = ["-","-","-","-","-"]
holdGuess = []
count = 0
correctWord = random.choice(five_letter_words)
print("Wordle\nUppercase = Letter is in the right spot in the word\nLowercase = Letter is in the word but not the right spot\nHyphen = Letter is not in word\nType 'stop' to quit\nYou have 5 tries")
while count < 5:
    guess = input("Guess: ")
    print(" ")
    if len(guess) == 5 and guess != correctWord:
        count += 1
        for letter in range(len(correctWord)):
            if guess[letter] == correctWord[letter]:
                array[letter] = guess[letter].upper()
            elif guess[letter] in correctWord:
                array[letter] = guess[letter].lower()
            else:
                array[letter] = "-"
                alphabet = alphabet.replace(guess[letter], ' ')
        holdGuess.append(''.join(array))
        print("Letters left = " + alphabet)
        for i in range(len(holdGuess)):
            print(holdGuess[i])
    elif guess == "stop" or guess == "Stop" or guess == "STOP":
        exit()
    elif guess == correctWord:
        holdGuess.append(correctWord.upper())
        for i in range(len(holdGuess)):
            print(holdGuess[i])
        print("Congrats! You Win!")
        exit()
    else:
        print("Please write a 5 letter word")
if count == 5:
    print("Sorry, you lose :(")
    print("The correct word was " + "'" + correctWord + "'")