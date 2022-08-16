import sys
sys.stdin = open('sample_input.txt')

tc = int(input())
for test in range(tc):
    a, b = list(map(str, input().split()))

    i = 0               # a의 인덱스
    count = 0           # 입력횟수
    while i<len(a):                 # 인덱스값이 전체 길이보다 작을때 까지
        if a[i] == b[0]:            # a[i]가 b의 첫글자와 같을때 탐색시작
            if a[i:i+len(b)] == b:  # b가 a안에 있을때
                count+=1            # i를 1이 아닌 b의 길이만큼 증가하고 count는 1번만 올린다.
                i += len(b)
            else:
                i += 1              # b와 다를때 count 1번
                count += 1
        else:
            count +=1               # b의 첫글자와 다를 경우도 count 1
            i+=1
    print(f'#{test+1} {count}')

