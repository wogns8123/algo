arr = [1,2,3]
target = 2
i = 0
while i < len(arr) and arr[i] != target:
    i+=1
if i<len(arr):
    print(i)
else:
    print(-1)

def binary(arr,start,end,key):
    start = 0
    end = len(arr)-1
    if start>end:
        return -1
    else:
        mid = (start+end)//2
        if key == arr[mid]:
            return arr[mid]
        elif key>arr[mid]:
            return binary(arr,mid+1,end,key)
        elif key<arr[mid]:
            return binary(arr,start,mid-1,key)

# n = len(arr)
# a = []
# for i in range(1<<n):
#     b=[]
#     for j in range(n):
#         if i & (1<<j):
#             b.append(arr[j])
#     a.append(b)
# print(a)