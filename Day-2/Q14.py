'''
Q14. Takes an input array of numbers and return a new array,
sorted in ascending order (smallest to biggest).

  If the function's argument is null, an empty array, or undefined;
  return an empty array.
 
  Examples
    [1, 2, 10, 50, 5] ➞ [1, 2, 5, 10, 50]

    [80, 29, 4, -95, -24, 85] ➞ [-95, -24, 4, 29, 80, 85]

    [] ➞ []
'''
#different approch
#sorter = lambda arr : sorted(arr)

examples = [[1, 2, 10, 50, 5],
            [80, 29, 4, -95, -24, 85],
            []]
for i in examples:
    print(i, '➞', sorted(i))
