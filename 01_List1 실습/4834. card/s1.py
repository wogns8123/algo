import sys
sys.stdin = open('input.txt')

tc = int(input())
for i in range(tc):
    number_dic = {}
    n = int(input())
    s = list(input())
    for number in s:
        if number in number_dic:
            number_dic[number] += 1
        else:
            number_dic[number] = 1
    a = [k for k, v in number_dic.items() if max(number_dic.values()) == v]
    print(f'#{i+1} {max(a)} {max(number_dic.values())}')
