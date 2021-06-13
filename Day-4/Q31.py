# Q31 Write a program  that takes an array of arrays with numbers. 
# Return a new (single) array with the largest numbers of each.

#   Examples
#     ([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]) ➞ [7, 90, 2]

#     ([[-34, -54, -74], [-32, -2, -65], [-54, 7, -43]]) ➞ [-34, -2, 7]

#     ([[0.4321, 0.7634, 0.652], [1.324, 9.32, 2.5423, 6.4314], [9, 3, 6, 3]]) ➞ [0.7634, 9.32, 9]

def myMax(arrOfArrays):
    ans=[]
    for arr in arrOfArrays:
        largest = -99999999
        for i in arr:
            if i > largest:
                largest = i
        ans.append(largest)
    return ans

examples = [[[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]],[[-34, -54, -74], [-32, -2, -65], [-54, 7, -43]],[[0.4321, 0.7634, 0.652], [1.324, 9.32, 2.5423, 6.4314], [9, 3, 6, 3]]]
for example in examples:
    print(example,'➞ ',myMax(example))
