import sys
sys.stdin = open('input.txt')

def triangle(n):
    result = []
    for i in range(n):  # 반복
        arr = []
        for j in range(i + 1):
            if j == 0 or j == i:  # 양 끝에 1
                arr.append(1)
            else:
                arr.append(result[i - 1][j - 1] + result[i - 1][j])  # 위의 값을 더한게 아래층 값
        result.append(arr)
    return result

tc = int(input())
for test in range(tc):
    n = int(input())
    print(f'#{test + 1}')
    for i in triangle(n):
        print(*i)
