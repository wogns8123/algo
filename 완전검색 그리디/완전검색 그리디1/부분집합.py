arr = [3,6,7,1,5,4]
n = len(arr)
result = []
for i in range(1<<n):
    subset = []
    for j in range(n):  # j번 비트가 0이 아니면 arr[j]의 부분집합 원소
        if i & (1<<j):
            subset.append(arr[j])
    result.append(subset)
print(result)
