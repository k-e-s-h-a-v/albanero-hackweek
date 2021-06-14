# Q.49 Given an array of distinct positive integers, 
# print all triplets that form an arithmetic progression with an integral common difference.
# Examples:
# Input:  A[] = { 5, 8, 9, 11, 12, 15 }
# Output:
# 5 8 11
# 9 12 15
# Input:  A[] = { 1, 3, 5, 6, 8, 9, 15 }
# Output:
# 1 3 5
# 1 5 9
# 3 6 9
# 1 8 15
# 3 9 15

def myBSort(myList):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(myList) - 1):
            if myList[i] > myList[i + 1]:
                swapped = True
                myList[i], myList[i + 1] = myList[i + 1], myList[i]
    return myList

def APtriplets(A):
    if len(A) < 3:
        return

    A = myBSort(A)

    for j in range(1, len(A) - 1):
        i = j - 1
        k = j + 1
        while i >= 0 and k < len(A):
            if A[i] + A[k] == 2 * A[j]:
                print((A[i], A[j], A[k]))
                k += 1
                i -= 1
            elif A[i] + A[k] < 2 * A[j]:
                k += 1
            else:
                i -= 1
 
 
examples = [[5, 8, 9, 11, 12, 15],[1, 3, 5, 6, 8, 9, 15]]
for example in examples:
    print(example)
    APtriplets(example)
