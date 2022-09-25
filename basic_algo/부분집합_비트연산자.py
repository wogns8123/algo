arr = [3,6,7,1,5,4]

# n = len(arr)
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j],end=', ')
#         print()


n = len(arr)
result = []
for i in range(1<<n):
    subset = []
    for j in range(n):
        if i&(1<<j):
            subset.append(arr[j])
    result.append(subset)
print(result)