def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):
    if n:
        inorder(ch1[n])
        print(n,end=' ')
        inorder(ch2[n])

def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n,end= ' ')

V, E = map(int,input().split())
arr = list(map(int,input().split()))
ch1=[0]*(V+1)
ch2=[0]*(V+1)
for i in range(0,E*2,2):
    p, c = arr[i], arr[i+1]
    if ch1[p] ==0:
        ch1[p] = c
    else:
        ch2[p] = c
print("전위 순회 :",end='')
preorder(1)
print()
print("중위 순회 :",end='')
inorder(1)
print()
print("후위 순회 :",end='')
postorder(1)
