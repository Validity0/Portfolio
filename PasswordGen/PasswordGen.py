import string;
import random;
'''takes input, found online'''
def PasswordGen(stringLength):
    '''puts letters digits and symbols in a string'''
    passwordCharacter = string.ascii_letters + string.digits + string.punctuation;
    '''loops and joins every character'''
    return ''.join(random.choice(passwordCharacter) for i in range(stringLength))

'''homemade'''
"""def RandomChar():
    '''prints'''
    print('Your New Password is: ', end="")
    '''i and while loop'''
    i = 1
    while i <= 8:
        '''Bit defines number or letter'''
        '''random choses a number and letter each space'''
        randomBit = random.randint(0,1);
        randomLetter = random.choice(string.ascii_letters);
        randomNumber = random.randint(0,9);
        '''bit if statement'''
        if randomBit == 0:
            print(randomNumber, end="");

        if randomBit == 1:
            print(randomLetter, end="");
        '''next space'''
        i += 1

RandomChar();"""
'''asks with input'''
stringLength = int(input('How long would you like your password to be?'));

'''prints plus password'''
print('Your Generated Password is:', PasswordGen(stringLength));