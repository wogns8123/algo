import sys
sys.stdin=open('sample_input.txt')

tc = int(input())

for test in range(tc):
    arr = [list(input()) for _ in range(5)]
    result = []
    print(f'#{test+1}',end=' ')
    max_len = 0
    for i in range(len(arr)):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    for i in range(max_len):
        for j in range(len(arr)):
            try:
                print(arr[j][i], end='')
            except:
                continue
    print()