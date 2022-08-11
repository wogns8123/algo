import sys

sys.stdin = open('sample_input.txt')

tc = int(input())
for test in range(tc):
    P, A, B = map(int, input().split())

    arr = list(range(1, P + 1))
    left = 1
    right = P

    A_count = 0
    while left <= right:
        A_middle = (left + right) // 2
        if A_middle == A:
            break
        elif A_middle > A:
            right = A_middle
        else:
            left = A_middle
        A_count += 1

    left = 1
    right = P
    B_count = 0
    while left <= right:
        B_middle = (left + right) // 2
        if B_middle == B:
            break
        elif B_middle > B:
            right = B_middle
        else:
            left = B_middle
        B_count += 1

    if A_count < B_count:
        print(f'#{test + 1} A')
    elif A_count > B_count:
        print(f'#{test + 1} B')
    else:
        print(f'#{test + 1} 0')
