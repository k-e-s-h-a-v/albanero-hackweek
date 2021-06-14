# Q.48 Given an integer array, 
# replace each element with the product of every other element 
# without using a division operator.
# Examples:
# Input:  { 1, 2, 3, 4, 5 }
# Output: { 120, 60, 40, 30, 24 }
# Input:  { 5, 3, 4, 2, 6, 8 }
# Output: { 1152, 1920, 1440, 2880, 960, 720 }

def arrayProduct(arr):
	n=len(arr)
	if n == 1:
		return arr
	temp = 1
	ans = [1]*n
	for i in range(n):
		ans[i] = temp
		temp = temp * arr[i]
	
	temp = 1
	for i in range(n - 1, -1, -1):
		ans[i] = ans[i] * temp
		temp = temp * arr[i]
	return ans

examples = [[1,2,3,4,5],[5, 3, 4, 2, 6, 8]]
for example in examples:
	print(example,end=' becomes ')
	print(arrayProduct(example))