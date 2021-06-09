def outlier(arr):
    temp=[i%2 for i in arr]
    if temp.count(0) < temp.count(1):
        return arr[temp.index(0)]
    else:
        return arr[temp.index(1)]

arr = list(map(int, input("Enter Space seperated array : ").split()))
print(outlier(arr))
