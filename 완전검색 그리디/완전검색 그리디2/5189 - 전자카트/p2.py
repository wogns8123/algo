import sys
sys.stdin = open('sample_input.txt')
from itertools import permutations

tc = int(input())
for test in range(tc):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    arr_basic = list(range(1,n))
    arr_permutaion = list(permutations(arr_basic))
    total_list = []
    for i in arr_permutaion:
        i = [0] + list(i) + [0]

        total = 0
        for j in range(n):
            total += arr[i[j]][i[j+1]]
        total_list.append(total)


    print(f'#{test+1} {min(total_list)}')




