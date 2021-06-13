# Q7. Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# Return the length of the longest (contiguous) subarray that contains only 1s. 
 
# Example 1:
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]

# Example 2:
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]


def max1s(A, K):
	count0 = left = ans = 0

	for i in range(len(A)):
		if A[i] == 0:
			count0 += 1

		while (count0 > K):
			if A[left] == 0:
				count0 -= 1
			left += 1
		ans = max(ans, i - left + 1)
	return ans



examples = [[1,1,1,0,0,0,1,1,1,1,0], [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]]
K = [2, 3]
for i in range(len(examples)):
    print(examples[i],'➞ ',max1s(examples[i], K[i]))
