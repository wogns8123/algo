import sys
sys.stdin=open('input.txt')

tc = int(input())
for test in range(tc):
    n, height = map(int,input().split())
    arr = list(map(int,input().split()))
    result = []
    height_list = []
    for i in range(1<<len(arr)):    # 부분집합 생성
        subset=[]
        for j in range(len(arr)):
            if i & (1<<j):
                subset.append(arr[j])
                if sum(subset) >= height:   # 부분집합의 합이 height 이상이면
                    height_list.append(sum(subset)) # 추가
    print(f'#{test + 1} {min(height_list) - height}')