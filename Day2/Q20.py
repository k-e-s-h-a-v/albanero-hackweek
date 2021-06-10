'''
Q20 Given an array of 10 numbers, return the maximum possible total made by summing just 5 of the 10 numbers.

  Examples
    [1, 1, 0, 1, 3, 10, 10, 10, 10, 1] ➞ 43

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 100] ➞ 100

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ➞ 40
  
  Notes
   You can select any 5 numbers from the given array to form maximum possible total.
   '''

maxsum5 = lambda arr : sum(sorted(arr)[-5:])
examples=[[1, 1, 0, 1, 3, 10, 10, 10, 10, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 100],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
for i in examples:
    print('for',i,'➞',maxsum5(i))
