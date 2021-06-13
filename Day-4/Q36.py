# Q36. You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
#  In how many distinct ways can you climb to the top?
#   Examples:
#   Input: n = 2
#   Output: 2
#   Explanation: There are two ways to climb to the top.
#   1. 1 step + 1 step
#   2. 2 steps
#   Input: n = 3
#   Output: 3
#   Explanation: There are three ways to climb to the top.
#   1. 1 step + 1 step + 1 step
#   2. 1 step + 2 steps
#   3. 2 steps + 1 step

def fib(n):
    fibtable={}
    if n in fibtable.keys():
        return fibtable[n]   
    if n==0 or n==1:
        value=n
    else:
        value = fib(n-1)+fib(n-2)   
    fibtable[n] = value
    return value

def steps(s):
    return fib(s + 1)

n = int(input("enter the number of steps : "))
print(steps(n))