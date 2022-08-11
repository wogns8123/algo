# 2중 배열의 모든 원소를 다 더하는 연습
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
s = 0
for i in range(N):
    for j in range(N):
        s +=arr[i][j]
print(s)
