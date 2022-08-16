import sys
sys.stdin=open('sample_input.txt')
tc = int(input())

for test in range(tc):
    str1 = input()
    str2 = input()
    count_list = []

    for i in str1:
        count = 0
        for j in str2:
            if j == i:
                count += 1
        count_list.append(count)
    print(f'#{test+1} {max(count_list)}')

