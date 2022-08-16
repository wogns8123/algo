import sys
sys.stdin = open('input.txt')

for test in range(1,11):
    num_length = int(input())
    arr = [input() for _ in range(8)]

    # 가로 체크
    total = 0
    for i in arr:
        count = 0
        for j in range(len(arr)-num_length+1):
            a = i[j:j+num_length]
            if a == a[::-1]:
                count+=1
        total+=count
    # print(total)

    # 세로 행렬 만들기
    new_arr = []
    for x in range(len(arr)):
        row = []
        for i in arr:
            row.append(i[x])
        new_arr.append((row))

    # 세로 체크
    total_y = 0
    for i in new_arr:
        count = 0
        for j in range(len(new_arr) - num_length + 1):
            a = i[j:j + num_length]
            if a == a[::-1]:
                count += 1
        total_y += count
    # print(total_y)
    print(f'#{test} {total+total_y}')
