# Q35. Write a program that takes an array of two numbers and determines
#  if the sum of the digits in each number are equal to each other.

#   Examples
#     ([105, 42]) ➞ true
#     # 1 + 0 + 5 = 6
#     # 4 + 2 = 6

#     ([21, 35]) ➞ false

#     ([0, 0]) ➞ true

def sumEqual(m, n):
    a=0
    while m or n:
        a += m%10 - n%10
        m//=10
        n//=10
    return not a

print(sumEqual(10, 560))