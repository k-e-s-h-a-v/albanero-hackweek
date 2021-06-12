'''
Q27. Write a program that takes two numbers as arguments (num, length) and 
returns an array of multiples of num until the array length reaches length.

  Examples
    arrayOfMultiples(7, 5) ➞ [7, 14, 21, 28, 35]

    arrayOfMultiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

    arrayOfMultiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]
  
  Notes
    Notice that num is also included in the returned array.
'''

def arrayOfMultiples(num, n): return [i*num for i in range(1,n+1)]

print(arrayOfMultiples(7,5))
print(arrayOfMultiples(12,10))
print(arrayOfMultiples(17,6))