# Q39 Given an integer array nums, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
#   Examples:
#   Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#   Output: 6
#   Explanation: [4,-1,2,1] has the largest sum = 6.
#   Input: nums = [1]
#   Output: 1
#   Input: nums = [5,4,-1,7,8]
#   Output: 23


def largestContiguousSub(arr):
    largest=-999999
    currentSum = 0
      
    for i in arr:
        currentSum += i
        if currentSum > largest:
            largest = currentSum
        if currentSum < 0:
            currentSum = 0 
    return largest

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(largestContiguousSub(arr))