import sys
sys.stdin = open('sample_input.txt')

def Find_Set(x):
    if x == p[x]:
        return x
    else:
        return Find_Set(p[x])

def Union(x,y):
    p[Find_Set(y)] = Find_Set(x)

tc = int(input())
for test in range(tc):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    p = [_ for _ in range(N+1)]

    for i in range(0,len(arr),2):
        Union(arr[i],arr[i+1])
    # result = [0, 1, 1, 3, 3, 5]
    result = []
    for i in range(1,N+1):
        result.append(Find_Set(i))
    # result = [1, 1, 3, 3, 5]
    result = set(result)
    # result = {1, 3, 5}
    print(f'#{test+1} {len(result)}')


