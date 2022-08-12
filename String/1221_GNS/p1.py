import sys
sys.stdin=open('GNS_test_input.txt')

tc = int(input())
for test in range(tc):
    num = input()
    arr = list(map(str, input().split()))
    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    new_numbers=[]

    for j in range(len(numbers)):
        for i in range(len(arr)):
            if arr[i] == numbers[j]:
                new_numbers.append(arr[i])

    print(f'#{test+1} ', end='')
    print(*new_numbers)