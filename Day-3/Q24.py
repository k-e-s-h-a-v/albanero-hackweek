'''
Q24. Suppose an image can be represented as a 2D array of 0s and 1s. 
Write a function to reverse an image. Replace the 0s with 1s and vice versa.

  Examples
    ([
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]
    ]) ➞ [
      [0, 1, 1],
      [1, 0, 1],
      [1, 1, 0]
    ]

    ([
      [1, 1, 1],
      [0, 0, 0]
    ]) ➞ [
      [0, 0, 0],
      [1, 1, 1]
    ]

    ([
      [1, 0, 0],
      [1, 0, 0]
    ]) ➞ [
      [0, 1, 1],
      [0, 1, 1]
    ]
'''
def rev(arr2d):
    for i in range(len(arr2d)):
        for j in range(len(arr2d[i])):
            arr2d[i][j]= int(not arr2d[i][j])
    return arr2d

examples = [
    [
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]
    ],
    [
      [1, 1, 1],
      [0, 0, 0]
    ],
    [
      [1, 0, 0],
      [1, 0, 0]
    ]
    ]
for example in examples:
    print(rev(example))