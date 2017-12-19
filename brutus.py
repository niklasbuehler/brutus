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
        if(decodedAscii < ord("A") or decodedAscii ):
            decodedAscii += 26
        if(decodedAscii > ord("Z")):
            decodedAscii -= 26
        decodedCharacters.append(chr(decodedAscii))

    decodedText = "".join(decodedCharacters)
    return decodedText

# main method
def main():
    # sys.argv[0] contains the scriptname
    path = sys.argv[1]
    encodedText = loadText(path)
    decodedText = decode(encodedText)
    print(decodedText)

main()
