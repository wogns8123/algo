import sys
sys.stdin=open('sample_input.txt')

tc = int(input())

for test in range(tc):
    arr = [list(input()) for _ in range(5)]
    result = []
    print(f'#{test+1}',end=' ')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            try:
                print(arr[j][i], end='')
            except:
                continue
    print()