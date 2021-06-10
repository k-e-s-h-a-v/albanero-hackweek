'''
Q17. Write a program that returns the sum of all even elements in a 2D matrix.
  Examples
    [
      [1, 0, 2],
      [5, 5, 7],
      [9, 4, 3]
    ] ➞ 6
    // 2 + 4 = 6

    [
      [1, 1],
      [1, 1]
    ] ➞ 0

    [
      [42, 9],
      [16, 8]
    ] ➞ 66
'''

sumer = lambda arr : sum([j for i in arr for j in i if not j%2])

examples = [
    [
      [1, 0, 2],
      [5, 5, 7],
      [9, 4, 3]
    ],
    [
      [1, 1],
      [1, 1]
    ],
    [
      [42, 9],
      [16, 8]
    ]]
for i in examples: 
  print(sumer(i))
