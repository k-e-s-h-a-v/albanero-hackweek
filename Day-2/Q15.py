'''
Q15. Take an input, array of numbers and return only the even values.

  Examples
    [1, 2, 3, 4, 5, 6, 7, 8] ➞ [2, 4, 6, 8]

    [43, 65, 23, 89, 53, 9, 6] ➞ [6]

    [718, 991, 449, 644, 380, 440] ➞ [718, 644, 380, 440]
  
  Notes
    Return all even numbers in the order they were given.
    All test cases contain valid numbers ranging from 1 to 3000.
'''
evenlover = lambda arr : [i for i in arr if not i%2]

examples = [[1, 2, 3, 4, 5, 6, 7, 8],
            [43, 65, 23, 89, 53, 9, 6],
            [718, 991, 449, 644, 380, 440]]
for i in examples:
    print('for',i,'➞',evenlover(i))
