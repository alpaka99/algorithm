arr = [5, 2, 6, 1, 9, 3, 7, 8, 4]

count = 0
for i in range(len(arr)-1):
    min_number = arr[i]
    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            count += 1
            arr[i], arr[j] = arr[j], arr[i]
            print("{} => {}, {} 교환".format(arr, i, j))
print("{}번 교환".format(count))