'''
Q13. Count the number of 1s in a given 2D array.

  Examples
    [
      [1, 0],
      [0, 0]
    ] ➞ 1

    [
      [1, 1, 1],
      [0, 0, 1],
      [1, 1, 1]
    ] ➞ 7

    [
      [1, 2, 3],
      [0, 2, 1],
      [5, 7, 33]
    ] ➞ 2
'''

examples = [
    [
      [1, 0],
      [0, 0]
    ],
    [
      [1, 1, 1],
      [0, 0, 1],
      [1, 1, 1]
    ],
    [
      [1, 2, 3],
      [0, 2, 1],
      [5, 7, 33]
    ]]

for arr in examples: print(sum([j for i in arr for j in i if j==1]))
