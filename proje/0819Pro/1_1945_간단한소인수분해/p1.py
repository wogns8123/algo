import sys

sys.stdin = open('input.txt')

tc = int(input())
for test in range(tc):
    N = int(input())
    count2, count3, count5, count7, count11 = 0, 0, 0, 0, 0

    while N >1:
        if N % 2 == 0:
            count2 += 1
            N = N // 2
        elif N % 3==0:
            count3 += 1
            N = N // 3
        elif N % 5==0:
            count5 += 1
            N = N // 5
        elif N % 7==0:
            count7 += 1
            N = N // 7
        elif N % 11==0:
            count11 += 1
            N = N // 11

    print(f'#{test+1} {count2} {count3} {count5} {count7} {count11}')
