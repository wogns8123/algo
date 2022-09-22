import sys

from itertools import permutations

sys.stdin = open('sample_input2.txt')

tc = int(input())
for test in range(tc):
    n = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]

    # 순열만들기
    p_arr = [i for i in range(1, n)]
    p_list = []
    route_all = []
    for per in permutations(p_arr):
        route = [0] + list(per) + [0]
        p_list.append(route)

    # 경로 # 1-2-3-1

    # 경로값

    for i in p_list:
        route = []
        for j in range(1, len(i)):
            route.append((i[j - 1], i[j]))
        route_all.append(route)

    min_n = (n ** 2) * 100

    for i in range(len(route_all)):
        total = 0
        for j in route_all[i]:  # j = (1,2),(2,3),(3,1)
            total += arr[j[0]][j[1]]
        if min_n > total:
            min_n = total
    print(f'#{test + 1} {min_n}')
