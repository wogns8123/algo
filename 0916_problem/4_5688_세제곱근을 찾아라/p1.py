import sys
sys.stdin = open('input.txt')

tc = int(input())
for test in range(tc):
    a = int(input())
    root = a**(1/3)
    root = round(root)

    if type(root) == int and root**3==a:
        print(f'#{test+1} {root}')
    else:
        print(f'#{test+1} -1')