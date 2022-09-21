tc = int(input())

for i in range(tc):
    number = int(input())                       # 입력하는 숫자의 개수
    numbers =list(map(int, input().split()))     # 숫자 입력
    # 최대값
    max_num = 0
    for idx in range(number):
        if max_num < numbers[idx]:
            max_num = numbers[idx]
    # 최소값
    min_num = numbers[0]
    for idx in range(number):
        if min_num > numbers[idx]:
            min_num = numbers[idx]
    print(f'#{i+1} {max_num - min_num}')





