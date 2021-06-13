# Q34. The digit distance between two numbers is the total value of the 
# difference between each pair of digits.

#   To illustrate:

#     (234, 489) ➞ 12
#     // Since |2 - 4| + |3 - 8| + |4 - 9| = 2 + 5 + 5
#   Write a program that returns the digit distance between two integers.

#   Examples
#     (121, 599) ➞ 19

#     (12, 12) ➞ 0

#     (10, 20) ➞ 1

#   Notes
#     Both integers will be exactly the same length.
#     All digits in num2 have to be higher than their counterparts in num1.

def myAbs(a, b):
    result = a-b
    if result < 0:
        return -result
    return result

def digitDistance(m,n):
    ans=0
    while m > 0 and n > 0:
        ans += myAbs(m % 10, n % 10)
        m//=10
        n//=10
    return ans

print(digitDistance(121,599))