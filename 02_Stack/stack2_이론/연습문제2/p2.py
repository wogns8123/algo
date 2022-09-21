arr = [1,2,3,4,5,6,7,8,9,10]
result = []
for i in range(1<<len(arr)):
    s_arr = []
    for j in range(len(arr)):
        if i&(1<<j):
            s_arr.append(arr[j])    # 부분집합 생성
    if sum(s_arr) == 10:
        result.append(s_arr)
print(result)
