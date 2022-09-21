def SelectionSort(arr,s):
    n = len(arr)
    if s == n-1:
        return
    minidx = s
    for i in range(s,n):
        if arr[minidx] > arr[i]:
            minidx = i
        arr[s], arr[minidx] = arr[minidx], arr[s]
    SelectionSort(arr,s+1)

arr = [2,4,6,1,9,8,7,0]
SelectionSort(arr,0)
print(arr)