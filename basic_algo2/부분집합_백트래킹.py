def constuct_candidates(a,k,input,c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a,k,input):
    global maxcandidates
    c = [0] 8 maxcandidates
    if k == input:
        process_solution(a,k)
    else:
        k+=1
        ncandidates = constuct_candidates(a,k,input,c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)

maxcandidates = 2
nmax = 4
a = [0] * nmax
backtrack(a,0,3)