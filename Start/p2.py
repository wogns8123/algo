import sys
sys.stdin=open('input.txt')

tc = int(input())
for test in range(tc):
    s = list(input())

    hex = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A':10,
        'B':11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    # 16진법 -> 10진법
    result = []
    for i in range(len(s)):
        result.append(hex[s[i]])
    # 10진법 -> 2진법
    bin_result = []
    for i in range(len(result)):
        a = bin(result[i])
        b = a[2:]
        while len(b)<4:
            b = '0'+b
        bin_result.append(b)

    cutting_text = ''.join(bin_result)
    # 2진법을 7개 단위로 자름
    lst = []
    for i in range(0,len(cutting_text),7):
        lst.append(cutting_text[i:i+7])
    # 자른 텍스트를 10진법으로 변환
    qa = []
    for i in lst:
        qa.append(int(i,2))
    print(*qa)




