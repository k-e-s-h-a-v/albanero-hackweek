'''
Q19.  Write a program that takes an array of numbers arr and a number n.
Return true if the sum of any two elements is equal to the given number.
Otherwise, return false.

  Examples
    ([10, 12, 4, 7, 9, 11], 16) ➞ true

    ([4, 5, 6, 7, 8, 9], 13) ➞ true

    ([0, 98, 76, 23], 174) ➞ true

    ([0, 9, 7, 23, 19, 18, 17, 66], 39) ➞ false

    ([2, 8, 9, 12, 45, 78], 1) ➞ false
    
'''

from itertools import permutations as per
arr = list(map(int, input('Enter the space seperated array : ').split()))
num = int(input('Enter the number : '))
def ret(arr, num):
    for i in map(list,per(arr, 2)):
        if sum(i)==num:
            return True
    return False
print(ret(arr, num))
