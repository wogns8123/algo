arr = [3,6,7,1,5,4]

n = len(arr)
for i in range(1<<n):       # 1<< n 부분집합의 개수
    for j in range(n):      # 원소의 수만큼 비트 비교
        if i&(1<<j):        # i의 j번 비트가 1인 경우
            print(arr[j],end=', ')  # j번 원소 출력력    print()
print()