import sys
sys.stdin = open('sample_input.txt')

tc =int(input())
for test in range(tc):
    n = float(input())
    result = []

    for i in range(12):     # 문제 조건 : 12 자리 이상일 경우 overflow
        if n >= 2**(-(i+1)):
            n-=2**(-(i+1))
            result.append('1')
            if n == 0:      # 결과가 0이 되면 break
                break
        else:               # 2**(-(i+1) 보다 작으면 0
            result.append('0')

    if n==0:
        result = ''.join(result)
        print(f'#{test+1} {result}')
    else:
        print(f'#{test+1} overflow')
