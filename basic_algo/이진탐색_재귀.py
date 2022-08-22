def binary_search(arr,start,end,target):
    if start>end:
        return -1

    mid = (start + end)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr,start,mid-1,target)
    else:
        return binary_search(arr,mid+1,end,target)

