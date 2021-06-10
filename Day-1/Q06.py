def AP(first, diff, n):
    ap=[]
    for i in range(n):
        ap.append(str(first + i*diff))
    return ap
first = int(input('Enter the first element : '))
diff = int(input('Enter the common difference : '))
n = int(input('Enter number of elements : '))
print(', '.join(AP(first, diff, n)))
