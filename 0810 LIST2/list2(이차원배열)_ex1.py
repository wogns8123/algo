N = 3   # 행
M = 4   # 열
# N개의 원소를 갖는 0으로 초기화된 1차원 배열
arr1 = [0]*N
# 크기가 N*M이고 0으로 초기화된 2차원 배열
arr2 = [[0]*M for i in range(N)]
print(arr2)
# 단순 곱하기는 얕은 복사가 되기때문에 사용X
# arr3 = [[0]*M]*N
# arr3[0][0] = 1
# print(arr3)

arr3 = [[1],[2,3],[3,4,5]]
print(arr3)
