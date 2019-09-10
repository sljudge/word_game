VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    LETTER_SCORE = {}
    WORD_SCORE = {}
    total = 0
    
    print (word)
    
    # Create dictionary from word showing number of occurences
    for letter in word:
        if letter in LETTER_SCORE:
            LETTER_SCORE[letter] += 1
        else:
            LETTER_SCORE[letter] = 1
    print (LETTER_SCORE)

    
    # Assign values to letters in dictionary AND total score for word
    for value in LETTER_SCORE:
        LETTER_SCORE[value] = SCRABBLE_LETTER_VALUES[value] * LETTER_SCORE[value]
        total += int(LETTER_SCORE[value])
    print (total)
    
    # Add bonus
    if len(word) == n:
        total = total * len(word)
        total += 50
    else:
        total = total * len(word)
    
    print (total)
    return LETTER_SCORE
    
    
    
print (getWordScore('waybill', HAND_SIZE))




    