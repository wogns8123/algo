import sys
sys.stdin=open('sample_input.txt')

def paper(n):
    if memo[n] == 0:
        memo[n] = paper(n-1)+2*(paper(n-2))
    return memo[n]

memo = [0]*100
memo[0] = 1
memo[1] = 3

tc = int(input())
for test in range(tc):
    num = int(input())
    num_2 = num//10

    print(f'#{test+1} {paper(num_2-1)}')