def depth_counter(strng):
    count, depth=0, 0
    for element in strng:
        if element == '(':
            count+=1
        elif element == ')':
            count-=1
    depth = max(depth,count)
    return depth

s = input('Enter the string to know its depth' )
print(depth_counter(s))
