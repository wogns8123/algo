arr = [3,4,5,6,7,8,9,10]
# def binary_search(arr,x):
#     start = 0
#     end = len(arr)-1
#
#     while start <= end:
#         mid = (start+end)//2
#
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             start = mid+1
#         else:
#             end = mid-1
#     return -1

def binary_search(arr,target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if target == arr[mid]:
            return mid
        elif arr[mid] < target:
            start = mid +1
        elif arr[mid] > target:
            end = mid-1
    return -1

print(binary_search(arr,10))

