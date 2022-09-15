import sys

sys.stdin = open('input.txt')

test = int(input())
for test_case in range(test):
    n, m, l = map(int, input().split())
    arr = [0] * (n + 2)  # 값을 저장할 리스트


    for _ in range(m):
        leap_num, number = map(int, input().split())
        arr[leap_num] = number      # leap node에 값을 저장
    while True:
        for i in range(n//2+1):
            if arr[2*i] != 0:       # 자식노드가 있을 때
                arr[i] = arr[2*i]+arr[2*i+1]    # 부모값 저장
        if arr[l] != 0:
            break

    print(f'#{test_case+1} {arr[l]}')