from ps4a import *

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    total_score = 0
    
    # As long as there are still letters left in the hand:
    inHand = True
    while inHand:
        if calculateHandlen(hand) != 0:
            # Display the hand
            displayHand(hand)
            # Ask user for input
            word = input ("Enter word, or a \".\" to indicate that you are finished: ")
            # If the input is a single period:
            if word == ".":
                # End the game (break out of the loop)
                print ()
                inHand = False
            # Otherwise (the input is not a single period):
            else:
                # If the word is not valid:
                if not isValidWord(word, hand, wordList):
                    # Reject invalid word (print a message followed by a blank line)
                    print ("Invalid word, please try again.")
                    print ()
                # Otherwise (the word is valid):
                else:
                    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                    total_score += getWordScore(word,n)
                    print ("\"" + word + "\"" + " earned " + str(getWordScore(word, n)) + " points. Total: " + str(total_score) + " points.")
                    print ()
                    # Update the hand 
                    hand = updateHand(hand, word)
        else:
            inHand = False
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) == 0:
        print ("Run out of letters. Total score: " + str(total_score))
    else:
        print ("Goodbye! Total score: " + str(total_score))

wordList = loadWords()
playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)