# Q.44 Given an array of integers, update every element with multiplication of preious 
# and next elements with following exceptions. 
# Note: a) First element is replaced by multiplication of first and second. 
#       b) Last element is replaced by multiplication of last and second last.
# Examples:
# Input:  [2, 3, 4, 5, 6]
# Output: [6, 8, 15, 24, 30]
# // We get the above output using following
# // arr[] = {2*3, 2*4, 3*5, 4*6, 5*6} 

# Input:  [2, 4, 3, 6, 7, 4, 2]
# Output: [8, 6, 24, 21, 24, 14, 8]
# // We get the above output using following
# // arr[] = {2*4, 2*3, 4*6, 3*7, 6*4, 7*2, 4*2}


def update(arr):

    if len(arr) <= 1:
        return arr

    pre = arr[0]
    arr[0] = arr[0] * arr[1]

    for i in range(1, len(arr)-1):
        curr = arr[i]
        arr[i] = pre * arr[i+1]
        pre = curr

    arr[-1] = pre * arr[-1]
    return arr

examples = [[2, 3, 4, 5, 6], [2, 4, 3, 6, 7, 4, 2],[2,3,7]]
for example in examples:
    print(example)
    print('➞ ', update(example))