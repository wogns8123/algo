import sys
sys.stdin = open('input.txt')


tc = int(input())
def f(i, n):
    if i == n:
        return
    else:
        for j in range(n):
            if visited[j] == 0:
                visited[j] = 1
                p[i] = arr[j]
                f(i + 1, n)
                visited[j] = 0

def run(arr):
    n = int(arr[0])
    for i in range(1, len(arr)):
        if n+1 != int(arr[i]):
            return False
        n = int(arr[i])
    return True

def Triplet(arr):
    n = arr[0]
    if arr.count(n) == len(arr):
        return True
    return False

for test in range(tc):
    arr = list(input())
    n = len(arr)
    p = [0] * n
    visited = [0] * n
    f(0, n)
    print(p)

