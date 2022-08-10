N = int(input())
arr =[list(map(int,input().split())) for _ in range(N)]
# 1
s = 0
for i in range(N):
    for j in range(N):
        if i == j:
            s += arr[i][j]
print(s)
# 2
s = 0
for i in range(N):
    s += arr[i][i]
print(s)
# 3 대각선
s = 0
for i in range(N):
    for j in range(N):
        if i+j == 3:
            s += arr[i][j]
print(s)
# 4 대각선
s = 0
for i in range(N):
    s += arr[i][N-1-i]
# X자
s = 0
for i in range(N):
    s += arr[i][N-1-i]
    s += arr[i][i]
    s = s - arr[N//2][[N//2]]
print(s)


'''
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''