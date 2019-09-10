# from update_hand import updateHand

def checkHand(word,hand):
    """
    Ensure that there are sufficient numbers of each letter to make word.
    Returns either True or False.
    """
    UPDATED_DICT = hand.copy()
    print (UPDATED_DICT)
    
    for letter in word:
        if UPDATED_DICT[letter] > 1:
            for value in range(UPDATED_DICT[letter]-1, UPDATED_DICT[letter]):
                UPDATED_DICT[letter] = UPDATED_DICT.get(letter,value)-1
            print (letter)
            print (UPDATED_DICT)
        elif UPDATED_DICT[letter] == 1:
            for value in range(UPDATED_DICT[letter]):
                UPDATED_DICT[letter] = UPDATED_DICT.get(letter,value)-1
            print (letter)
            print (UPDATED_DICT)
        else:
            print ('No more letters!')
            return False
    return True

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    tempWord = word[:]
    tempHand = hand.copy()
    
    try:  
        if checkHand(tempWord,tempHand) and word in wordList:
            return True
        else:
            return False
    except KeyError:
        print('KeyError')
        return False

word = ''
hand = {'e': 1, 'a': 3, 't': 1, 'p': 2, 'r': 1, 'u': 1, 'b':1, 'o':1, 's':2}
wordList = ['quail','boss', 'bo', 'rapture', 'bos']
print (isValidWord(word, hand, wordList))
        
        