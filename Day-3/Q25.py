'''
Q25. An isogram is a word that has no duplicate letters. 
Write a program that takes a string and returns either true or false 
depending on whether or not it's an "isogram".

  Examples
    ("Algorism") ➞ true

    ("PasSword") ➞ false
    // Not case sensitive.

    ("Consecutive") ➞ false
  
  Notes
    Ignore letter case (should not be case sensitive).
    All test cases contain valid one word strings.
'''

def isogramCheck(word):
    word = word.lower()
    uniqueLetters = []
 
    for letter in word:
        if letter in uniqueLetters:
            return False
        uniqueLetters.append(letter)
    return True

Examples = ['Algorism','PasSword','Consecutive']
for testCase in Examples:
    print(testCase,'➞',isogramCheck(testCase))