import sys
sys.stdin=open('sample_input.txt')
from collections import deque

tc = int(input())
for test in range(tc):
    container, trailer = map(int,input().split())
    container_list = list(map(int,input().split()))     #  화물무게
    trailer_list = list(map(int,input().split()))       # 적재 용량
    trailer_list.sort(reverse=True)             # 최대값부터
    container_list.sort(reverse=True)           # 최대값부터

    result = []

    while True:
        if len(trailer_list) != 0:                      # 트럭이 있으면
            if trailer_list[0] < container_list[0]:     # 맨 앞 값 비교해서 못 실으면 제거
                container_list.pop(0)
            else:
                result.append(container_list.pop(0))    # 적재가능하면 적재
                trailer_list.pop(0)
        else:
            break

        if len(container_list) == 0:                    # 실은 화물 없으면 break
            break
    print(f'#{test+1} {sum(result)}')

