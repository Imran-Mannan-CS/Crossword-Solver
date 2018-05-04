import pprint



def getDictionary():
    with open('Dictionary.txt','r') as dictionaryOpen:
        dictionary = dictionaryOpen.read().split()
    return dictionary
    

def checkWord (testWord,dictionary):
    
    nonBlanks = len(testWord)-testWord.count(' ')
    for word in dictionary:
        incLetter = 0
        incMatch = 0
        if len (word) == len (testWord):
            for letter in testWord:
                if letter == word[incLetter]:
                    incMatch += 1
                incLetter += 1
            if incMatch == nonBlanks:
                print (word)
                input()
                
    return
        
def main():
    dictionary = getDictionary()
    q = 'y'
    while 'n' not in q:
        testWord = input ("Please input a word to solve.\nUse Spaces to signify unkown letters: ")
        checkWord (testWord,dictionary)
        q = input("Test another word? y/n")
        
main()