import sys

sys.stdin = open('sample_input.txt')

def inorder(n):             # 중위 순회
    global count
    if n:
        inorder(ch1[n])
        # print(n, end=' ')
        count.append(n)
        inorder(ch2[n])

tc = int(input())
for test in range(tc):
    n = int(input())
    arr = list(range(n + 1))
    count = []
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)
    E = n - 1
    for i in range(1, n // 2 + 1):
        try:                    # 마지막 arr[2*i+1]가 없을 때 index error
            p, c1, c2 = arr[i], arr[2 * i], arr[2 * i + 1]
            if ch1[p] == 0:
                ch1[p] = c1
                ch2[p] = c2
        except:
            p, c1 = arr[i], arr[2 * i]
            if ch1[p] == 0:
                ch1[p] = c1
    inorder(1)              # 중위순회

    print(f'#{test+1} {count.index(1)+1} {count.index(n//2)+1}')

