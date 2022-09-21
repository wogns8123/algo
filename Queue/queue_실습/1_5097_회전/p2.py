import sys
sys.stdin = open('sample_input.txt')

tc =int(input())
for test in range(tc):
    a,b =map(int,input().split())       # a : 배열의 수 / b : 반복 수
    arr = list(map(int,input().split()))

    for i in range(b):
        num = arr.pop(0)    # 앞의 글자를 빼서
        arr.append(num)     # 배열끝에 추가
    print(f'#{test+1} {arr[0]}')