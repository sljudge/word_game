def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    length = 0
    
    for key in hand:
        if hand[key] != 0:
            length += hand[key]
    
    return length
    
print (calculateHandlen({'e': 1, 'a': 3, 't': 1, 'p': 1, 'r': 1}))