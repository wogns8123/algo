import sys
sys.stdin = open('input.txt')

tc = int(input())
for test in range(tc):
    s = input()
    result = []
    for i in range(0,len(s),7):
        result.append(s[i:i+7])
    result2 = []
    for i in result:
        result2.append(int(i,2))
    print(*result2)

