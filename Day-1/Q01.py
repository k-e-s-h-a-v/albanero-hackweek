from random import randint as rc
from collections import Counter as jmap  #to count occurances

n=int(input('Enter n : '))
strng=''
while len(strng)!= n:
    k=chr(rc(ord('a'),ord('z')))
    if strng.count(k)%2:
        strng+=k*2
    else:
        strng+=k

print(strng)
print(jmap(strng))  #just to check number of occurances
