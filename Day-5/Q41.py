# Q.41 Count the frequency of the all the elements in an array.
# Examples:
# Input: [1,2,3,1,4,3,5,6,3,4,2,4,5,3]
# Output:
# 1->2,
# 2->2,
# 3->4,
# 4->3,
# 5->2,
# 6->1
# Input: [1,2,3,4]
# Output:
# 1->1,
# 2->1,
# 3->1,
# 4->1


def mySet(arr):
    new = []
    for i in arr:
        if i not in new:
            new.append(i)
    return new

examples = [[1,2,3,1,4,3,5,6,3,4,2,4,5,3], [1,2,3,4]]
for example in examples:
    for i in mySet(example):
        count = 0
        for element in example:
            if i== element:
                count += 1
        print(i,'➞ ',count)
    print('###########################')
