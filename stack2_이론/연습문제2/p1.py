<<<<<<< HEAD
# 기존 비트연산자를 이용한 부분집합
arr = [1,2,3,4,5,6,7,8,9,10]
result = []
for i in range(1<<len(arr)):
    s_arr = []
    for j in range(len(arr)):
        if i&(1<<j):
            s_arr.append(arr[j])    # 부분집합 생성
    if sum(s_arr) == 10:
        result.append(s_arr)
print(result)
=======
def f(i,N):
    global answer
    if i == N:
        s=0
        for i in range(N):
            if bit[i]:
                s += A[i]
                # print(A[i], end = ' ')
        # print()
        if s==10:
            answer+=1
            for i in range(N):
                if bit[i]:
                    print(A[i], end = ' ')
            print()

    else:
        bit[i] =1
        f(i+1,N)
        bit[i] =0
        f(i+1,N)

A=[1,2,3,4,5,6,7,8,9,10]
bit = [0] *10
answer = 0
f(0,10)
print(answer)
>>>>>>> 64e822a1329e866f44c167d58fc620ece17ea32b
