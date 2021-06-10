'''
Q16. Take input, an array of positive and negative numbers.
Return an array where the first element is the count of positive numbers
and the second element is the sum of negative numbers.

  Examples
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15] ➞ [10, -65]
    // There are a total of 10 positive numbers.
    // The sum of all negative numbers equals -65.

    [92, 6, 73, -77, 81, -90, 99, 8, -85, 34] ➞ [7, -252]

    [91, -4, 80, -73, -28] ➞ [2, -105]

    [] ➞ []
  
  Notes
    If given an empty array, return an empty array: []
    0 is not positive.
'''

def magic(arr):
  if arr==[]: return []
  count, summ = 0, 0
  for i in arr:
    if i>0:
      count+=1
    else:
      summ+=i
  return [count, summ]

examples = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],
            [92, 6, 73, -77, 81, -90, 99, 8, -85, 34],
            [91, -4, 80, -73, -28],
            [0, 0, 0],
            []]

for i in examples:
  print(magic(i))
