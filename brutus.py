####### BRUTUS.PY #######
# CAESAR CIPHER DECODER #
#########################

# Usage:         python brutus.py path/to/input.txt
# Print to file: python brutus.py path/to/input.txt > path/to/output.txt

import sys
import re

# loads a string from a file
def loadText(filename):
    file = open(filename, "r")
    text = file.read()
    return text

# formats the text to uppercase only and returns as list of characters
def getCharacters(text):
    text = text.upper()
    return list(text)

# returns the most common letters in a list
def most_common_letter(text):
    text = re.sub('[^A-Za-z]+', '', text).upper()
    lst = list(text)
    return max(set(lst), key=lst.count)

# decodes the caesar cipher by assuming the most common letter is an 'E'
def decode(encodedText):
    assumedE = most_common_letter(encodedText)
    characters = getCharacters(encodedText)

    key = ord(assumedE) - ord("E")

    decodedCharacters = []
    for character in characters:
        encodedAscii = ord(character)

        # only shift letters
        if(encodedAscii < ord("A") or encodedAscii > ord("Z")):
            decodedCharacters.append(character)
            continue

        decodedAscii = encodedAscii - key

        # wrap shift
        if(decodedAscii < ord("A")):
            decodedAscii += 26
        if(decodedAscii > ord("Z")):
            decodedAscii -= 26
        decodedCharacters.append(chr(decodedAscii))

    decodedText = "".join(decodedCharacters)
    return decodedText

def encode(decodedText, key):
    characters = getCharacters(decodedText)

    encodedCharacters = []
    for character in characters:
        decodedAscii = ord(character)

        # only shift letters
        if(decodedAscii < ord("A") or decodedAscii > ord("Z")):
            encodedCharacters.append(character)
            continue

        encodedAscii = decodedAscii + key

        # wrap shift
        if(encodedAscii < ord("A")):
            encodedAscii += 26
        if(encodedAscii > ord("Z")):
            encodedAscii -= 26
        encodedCharacters.append(chr(encodedAscii))

    encodedText = "".join(encodedCharacters)
    return encodedText


# main method
def main():
    # sys.argv[0] contains the scriptname
    args = len(sys.argv)

    if(args == 1):
        print("missing arguments")
        print("add option -h for help")
        return

    command = sys.argv[1]

    if(command == "-d"):
        if(args != 3):
            print("missing arguments")
            print("add option -h for help")
            return
        path = sys.argv[2]
        encodedText = loadText(path)
        decodedText = decode(encodedText)
        print(decodedText)
    elif(command == "-e"):
        if(args != 4):
            print("missing arguments")
            print("add option -h for help")
            return
        path = sys.argv[2]
        key = int(sys.argv[3])
        decodedText = loadText(path)
        encodedText = encode(decodedText, key)
        print(encodedText)
    elif(command == "-h" or command == "--help"):
        print("options:")
        print("decoding: -d /path/to/file.txt")
        print("encoding: -e /path/to/file.txt key")

main()
