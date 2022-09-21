import sys
sys.stdin=open('input.txt')

tc =int(input())
for test in range(tc):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result_list = []
    for y in range(N-M+1):
        for x in range(N-M+1):
            # 0,0 부터 2,2까지
            total_list = []
            for i in range(M):
                total = 0
                for j in range(M):
                    total += arr[i+y][j+x]
                total_list.append(total)
            sum = 0
            for i in total_list:
                sum += i
            result_list.append(sum)
    max_value = 0
    for i in result_list:
        if i > max_value:
            i,max_value = max_value,i
    print(f'#{test+1} {max_value}')
