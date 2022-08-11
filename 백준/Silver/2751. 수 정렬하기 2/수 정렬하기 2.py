import sys
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr_sort = sorted(arr)
for i in arr_sort:
    print(i)