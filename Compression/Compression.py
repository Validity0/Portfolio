word = "aabbbbcdeeeefffg"
#output should be 2a4b1c1d4e3f1g

def encode(string):
    count = 0
    hashtable = {}
    letter = string[0]
    for i in string:
        if i != letter:
            hashtable[letter] = count
            count = 1
            letter = i
        else:
            count += 1
        hashtable[letter] = count

    encodedString = ''
    for i in hashtable:
        encodedString += str(hashtable[i]) + i
    return encodedString
encode(word)
print(encode(word))

def decode(string):
    decodedString = ""

    for i in reversed(string):
        if i.isdigit():
            number = int(i)
            decodedString += letter * number
        else:
            letter = i
    decodedString = decodedString[::-1]
    print(decodedString)
decode(encode(word))

