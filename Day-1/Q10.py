def evenOnly(arr): return list(filter(lambda i: i % 2 == 0, arr))

arr = list(map(int, input("Enter Space seperated array : ").split()))

print("Even ->",evenOnly(arr))
