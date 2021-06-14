# Q.50 Given an M X N matrix, print the matrix in spiral order.
# Example: 
# Input: 
# [  1   2   3   4  5 ]
# [ 16  17  18  19  6 ]
# [ 15  24  25  20  7 ]
# [ 14  23  22  21  8 ]
# [ 13  12  11  10  9 ]
# Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25



def topOrBottomRow(arr, tb):
    ret = arr[tb]
    del arr[tb]
    return ret, arr

def firstOrLastColumn(arr, fl):
    if isinstance(arr[0], list):
        temp=[]
        for i in arr:
            temp.append(i[fl])
            del i[fl]
        return temp, arr
    else:
        ret = arr[fl]
        del arr[fl]
        return ret, arr

arr=[
    [1, 2, 3, 4, 5], 
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
    ]

	
lst=[]
try:
    while arr:
        tmp, arr = topOrBottomRow(arr, 0)
        lst += tmp
        tmp, arr = firstOrLastColumn(arr, -1)
        lst += tmp
        tmp, arr = topOrBottomRow(arr, -1)
        lst += tmp[::-1]
        tmp, arr = firstOrLastColumn(arr, 0)
        lst += tmp[::-1]
except IndexError:
    for i in lst:
        print(i, end=' ')
