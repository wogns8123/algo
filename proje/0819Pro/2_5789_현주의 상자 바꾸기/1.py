import sys
sys.stdin=open('sample_input.txt')

tc =int(input())
for test in range(tc):
    N,Q = map(int,input().split())
    arr = [0] * N
    for i in range(1,Q+1):
        start, end = map(int,input().split())
        for j in range(start,end+1):
            arr[j-1] = i
    print(f'#{test + 1}',end=' ')
    for i in arr:
        print(i,end=' ')
    print()
