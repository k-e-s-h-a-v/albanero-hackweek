# Q32. A set is a collection of unique items. 
# A set can be formed from an array from removing all duplicate items.

#   [1, 3, 3, 5, 5, 5]
#   // original array

#   [1, 3, 5]
#   // original array transformed into a set
#   Write a program that sorts an array and removes all duplicate items from it.

#   Examples
#     ([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
#     ([4, 4, 4, 4]) ➞ [4]
#     ([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
#     ([3, 3, 3, 2, 1]) ➞ [1, 2, 3]

#   Notes
#     All arrays will have at least one element.
#     For this question, output an array, not a set.

def mySet(arr):
    newArray=[]
    for i in arr:
        if i not in newArray:
            newArray.append(i)
    return newArray

def myBSort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def sortSet(arr):
    return myBSort(mySet(arr))

examples = [[1, 3, 3, 5, 5],[4, 4, 4, 4],[5, 7, 8, 9, 10, 15],[3, 3, 3, 2, 1]]
for example in examples:
    print(example,'➞ ',sortSet(example))
