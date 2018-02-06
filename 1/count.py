import sys

arguments = sys.argv[1:]

def isVowel(char):
    if(char in 'aeiou'):
        return True
    return False

def isAlpha(char):
    return not isVowel(char)

if(len(arguments) < 2):
    print('''let\'s try this.
    python count.py [type] [string]
    [type] is type of char which you want to count in string.
        (vowel / alphabet / digit / lowercase / uppercase)
    [string] is input string.''')
else:
    typechar = arguments[0]
    string = arguments[1]
    count = 0
    if(typechar == 'vowel'):
        for char in string:
            if(isVowel(char)):
                count = count+1
    elif(typechar == 'alphabet'):
        for char in string:
            if(char.isalpha() and isAlpha(char)):
                count = count+1
    elif(typechar == 'digit'):
        for char in string:
            if(char.isdigit()):
                count = count+1
    elif(typechar == 'lowercase'):
        for char in string:
            if(char.islower()):
                count = count+1
    elif(typechar == 'uppercase'):
        for char in string:
            if(char.isupper()):
                count = count+1
    print(count)

