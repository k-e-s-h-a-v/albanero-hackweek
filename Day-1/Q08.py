# Q8. Given an array A of integers, we must modify the array in the following way: 
# we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  
# (We may choose the same index i multiple times.)
# Return the largest possible sum of the array after modifying it in this way.
 
# Example 1:
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].
# Example 2:
# Input: A = [3,-1,0,2], K = 3 
# Output: 6
# Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
# Example 3:
# Input: A = [2,-3,-1,5,-4], K = 2
# Output: 13
# Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].

def myBSort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def myMin(arr):
    m = 9999999
    for i in arr:
        if i < m:
            m = i
    return m

def mySum(arr):
    add = 0
    for i in arr:
        add+=i
    return add

def maxSum(arr,k):
    arr = myBSort(arr)
    for i in range(len(arr)):
        if arr[i]<0 and k>0:
            arr[i] = -arr[i]
            k-=1

    summ = mySum(arr)

    x = myMin(arr)

    if k%2:
        summ -= 2*x
    return summ

aexamples = [[4,2,3], [3,-1,0,2], [2,-3,-1,5,-4]]
kexamples = [1, 3, 2]
for i in range(len(aexamples)):
    print(aexamples[i],',',kexamples[i],'➞ ',maxSum(aexamples[i], kexamples[i]))
