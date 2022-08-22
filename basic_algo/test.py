s = 'abcdef'
search = 'a'

N = len(s)
M = len(search)

def bruteforce(s,search):
    i = 0   #s의 인덱스
    j = 0   # search의 인덱스
    while i<N and j<M:
        if s[i]!=search[j]:
            i = i-j
            j = -1
        i+=1
        j+=1
    if j == M:
        return i-M
    else:
        return -1
print(bruteforce(s,search))