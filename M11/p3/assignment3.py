# Assignment-3
'''
At this point, we have written code to generate a random hand and display that hand to the user. We can also ask the user for a word (Python's input) and score the word (using your getWordScore). However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game. A valid word is in the word list; and it is composed entirely of letters from the current hand. Implement the isValidWord function.

Testing: Make sure the test_isValidWord tests pass. In addition, you will want to test your implementation by calling it multiple times on the same hand - what should the correct behavior be? Additionally, the empty string ('') is not a valid word - if you code this function correctly, you shouldn't need an additional check for this condition.

Fill in the code for isValidWord in ps4a.py and be sure you've passed the appropriate tests in test_ps4a.py before pasting your function definition here.
'''

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    c_c=0
    l_l=len(wordList)

    if word in wordList:
        for i in hand:
            if i in word:
                c_c= c_c+1
    if c_c == l_l:
        return True
    return False
def main():
    word=input()
    n_n=int(input())
    adict={}
    for i in range(n_n):
        data=input()
        l_l=data.split()
        adict[l_l[0]]=int(l_l[1])
    l2_l=list(input().split())
    print(isValidWord(word,adict,l2_l))
if __name__== "__main__":
    main()
