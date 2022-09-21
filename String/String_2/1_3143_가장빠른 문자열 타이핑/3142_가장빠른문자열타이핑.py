import sys
sys.stdin = open('sample_input.txt')

tc = int(input())
for test in range(tc):
    a, b = list(map(str, input().split()))
    count = 0
    for i in range((len(a) - len(b)) + 1):
        if a[i:i + len(b)] == b:
            count += 1
            continue

    if count>=0:
        print(f'#{test + 1} {len(a) - (len(b) * count) + count}')
    else:
        print(f'#{test+1} {len(a)}')
