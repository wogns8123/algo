import sys
sys.stdin=open('input1.txt')
tc = int(input())

for test in range(tc):
    num = int(input())
    arr = list(input())
    count = 0
    count_list = []
    for i in range(num):
        if arr[i] == '1':
            count+=1
        else:
            count = 0
        count_list.append(count)

    print(f'#{test+1} {max(count_list)}')