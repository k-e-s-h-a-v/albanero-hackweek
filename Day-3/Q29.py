'''
Q29. Write a program that squares every digit of a number.

  Examples
    (9119) ➞ 811181

    (2483) ➞ 416649

    (3212) ➞ 9414
  Notes
    The function receives an integer and must return an integer.
'''

def squares(num):
  num=str(num)
  ans=''
  for i in num:
    ans+=str(int(i)*int(i))
  return int(ans)

examples = [9119,2483,3212]
for i in examples:
  print('for',i,'➞ ',squares(i))