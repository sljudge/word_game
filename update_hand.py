def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    # ***Stops at 0
    UPDATED_DICT = hand.copy()

    for letter in word:
        if UPDATED_DICT[letter] > 1:
            for value in range(1):
                UPDATED_DICT[letter] = UPDATED_DICT.get(letter,(value))-1
        else:
            for value in range(UPDATED_DICT[letter]):
                UPDATED_DICT[letter] = UPDATED_DICT.get(letter,(value))-1

    return UPDATED_DICT
    
    # *******IMPROVED SOLUTION*************
    # 
    # tempHand = hand.copy()

    # for x in word:
    #     if x in tempHand and tempHand[x] > 0:
    #         for y in range(1):
    #             tempHand[x] = tempHand.get(x,y) - 1
    #             print tempHand
    #     else:
    #         return False
    
    # hand = tempHand
    # return True
    

word = 'rapture'
hand = {'e': 1, 'a': 3, 't': 1, 'p': 2, 'r': 1, 'u': 1}
wordList = ['quail','boss', 'bo', 'rapture']
print (updateHand(hand, word))
