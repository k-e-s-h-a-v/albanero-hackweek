# Q30. Write a program that returns the mean of all digits.
#   Examples
#     (42) ➞ 3

#     (12345) ➞ 3

#     (666) ➞ 6
  
#   Notes
#     The mean of all digits is the sum of digits / how many digits there are 
#     (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
#     The mean will always be an integer.

def mean(num):
    summ=0
    count=0
    while num:
        summ += num%10
        num = num//10
        count+=1
    return summ//count

examples = [42, 12345, 666]
for example in examples:
    print('for',example,'➞', mean(example))