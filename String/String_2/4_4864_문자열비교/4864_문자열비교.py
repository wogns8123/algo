import sys
sys.stdin = open('sample_input.txt')

tc = int(input())

for test in range(tc):
    str1 = input()
    str2 = input()
    result = 0
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            result = 1
        else:
            result
    print(f'#{test+1} {result}')