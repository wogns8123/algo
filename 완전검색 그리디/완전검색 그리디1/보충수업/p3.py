import sys
sys.stdin = open('input.txt')

def swap(prize,i,j):
    # i to a
    prize_arr = [0] * prize_length
    for k in range(prize_length-1, -1, -1):
        prize_arr[k] = prize%10
        prize //= 10
    # swap
    prize_arr[i], prize_arr[j] = prize_arr[j], prize_arr[i]
    # a to i
    prize = 0
    for k in range(prize_length):
        prize = prize * 10 + prize_arr[k]
    # 0*10 + 2 => 2
    # 2*10 + 1 => 21
    # 21*10 + 3 => 213
    return prize


def find_max(n, k, prize):
    global ans, count
    count += 1
    for i in range(720):
        # memoization
        if memo[k][i] == 0:
            memo[k][i] = prize
            break
        # 가지치기
        elif memo[k][i] == prize:
            return

    if n == k:
        if prize > ans:
            ans = prize
    else:  # 숫자판 길이에서 2개를 선택
        for i in range(prize_length - 1):
            for j in range(i + 1, prize_length):
                find_max(n, k + 1, swap(prize, i, j))


tc = int(input())
for test in range(tc):
    prize, N = map(int, input().split())
    ans = 0
    memo = [[0] * 720 for _ in range(N+1)]
    # 숫자판의 길이
    prize_length = 0
    temp = prize
    count = 0
    while temp:
        temp //= 10
        prize_length += 1

    find_max(N, 0, prize)
    print(f'#{test + 1} {ans}')
