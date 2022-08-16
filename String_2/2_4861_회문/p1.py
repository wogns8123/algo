import sys
sys.stdin = open('sample_input.txt')

tc = int(input())

for test in range(tc):
    n, m = list(map(int,input().split()))
    arr = [input() for _ in range(n)]
    # 가로
    for i in arr:
        for j in range(len(i)-m+1):
            a = i[j:j+m]
            if a == a[::-1]:
                print(f'#{test+1} {a}')

    # 세로 만들기
    new_arr = []
    for x in range(len(arr)):
        row = []
        for i in arr:
            row.append(i[x])
        new_arr.append((row))
    # 세로 탐색
    for i in new_arr:
        for j in range(len(i)-m+1):
            a = i[j:j+m]
            if a == a[::-1]:
                print(f"#{test+1} {''.join(a)}")
