# Q37. Given an integer num, return an array of the number of 1's 
# in the binary representation 
# of every number in the range [0, num].
#   Examples:
#   Input: num = 2
#   Output: [0,1,1]
#   Explanation:
#   0 --> 0
#   1 --> 1
#   2 --> 10
#   Input: num = 5
#   Output: [0,1,1,2,1,2]
#   Explanation:
#   0 --> 0
#   1 --> 1
#   2 --> 10
#   3 --> 11
#   4 --> 100
#   5 --> 101

def Binary1counter(n):
    ans=0
    while n:
        ans += n%2
        n//=2
    return ans
    
n = int(input())
lst=[]
for i in range(n+1):
    lst.append(Binary1counter(i))
print(lst)