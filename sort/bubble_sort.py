arr = [1, 2, 6, 8, 4, 5, 3, 7, 9]

n = len(arr)
for i in range(n - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)