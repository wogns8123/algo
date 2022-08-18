import sys
sys.stdin = open('sample_input.txt')
def paper_num(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper_num(n-1)+2*(paper_num(n-2))
tc = int(input())
for test in range(tc):
    num = int(input())
    num_2 = num//10
    print(f'#{test+1} {paper_num(num_2)}')