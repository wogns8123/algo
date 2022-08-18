import sys
sys.stdin=open('sample_input.txt')

def remove_s(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            return remove_s(s)
    else:
        return len(s)


tc = int(input())
for test in range(tc):
    s = list(input())

    print(f'#{test+1} {remove_s(s)}')



