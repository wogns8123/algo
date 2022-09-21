import sys
sys.stdin = open('sample_input.txt')

def preorder(n):    # 전위 순회
    global result
    if n:
        result.append(n)
        preorder(ch1[n])
        preorder(ch2[n])
    return result
tc = int(input())
for test in range(tc):
    E, N = map(int,input().split())
    arr = list(map(int,input().split()))
    V = E+1
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    result = []
    count = 0
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c


    print(f'#{test+1} {len(preorder(N))}')