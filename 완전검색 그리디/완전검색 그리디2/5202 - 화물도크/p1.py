import sys
sys.stdin = open('sample_input.txt')

tc = int(input())
for test in range(tc):
    n = int(input())
    sche = []
    for _ in range(n):
        start, end = map(int,input().split())
        sche.append((start,end))
    sche.sort(key = lambda x:x[1])      # 빨리 끝나는 순으로 정렬
    result = [sche[0]]

    for i in range(1,len(sche)):
        if sche[i][0]<result[-1][1]:
            pass
        else:
            result.append(sche[i])
    print(f'#{test+1} {len(result)}')
