'''
Q18. Write a program that finds each factor of a given number n. Your solution should return an array of the number(s) that meet this criteria.

  Examples
    (9) ➞ [1, 3, 9]
    // 9 has three factors 1, 3 and 9

    (12) ➞ [1, 2, 3, 4, 6, 12]

    (20) ➞ [1, 2, 4, 5, 10, 20]

    (0) ➞ []
'''

n = int(input('Enter a Number to show its factors : '))
factors=[]
for i in range(1,n+1):
  if not n%i:
    factors.append(i)
print(factors)
