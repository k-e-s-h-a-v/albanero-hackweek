'''
Q26. A repdigit is a positive number composed out of the same digit. 
Write a program that takes an integer and returns whether it's a repdigit or not.

  Examples
    (66) ➞ true

    (0) ➞ true

    (-11) ➞ false

  Notes
    The number 0 should return true (even though it's not a positive number).
    Check the Resources tab for more info on repdigits.
'''

def isRepDigit(num):
    if num<0:
        return False
    while num:
        temp = num % 10
        num = num // 10
        if temp != num % 10 and num!=0:
            return False
    return True

Examples = [66,0,533,-11]
for example in Examples:
    print('(',example,')','➞ ',isRepDigit(example))
