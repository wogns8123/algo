# import sys
# sys.stdin = open('sample_input.txt')

hex = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A':10,
        'B':11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

tc = int(input())
for test in range(tc):
    n, s = input().split()
    n = int(n)
    s = list(s)

    result_10 = []
    # 10진수로 변환
    for i in range(n):
        result_10.append(hex[s[i]])
    # 2진수로 변환
    result_2 = []
    for i in range(n):
        a = bin(result_10[i])
        b = a[2:]
        while len(b) < 4:
            b = '0' + b
        result_2.append(b)
    result = ''.join(result_2)
    print(f'#{test+1} {result}')