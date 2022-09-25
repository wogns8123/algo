def preorder(n):
    if n:
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)
E = int(input())
V = E+1
ch1 = [0] *(V+1)
ch2 = [0]* (V+1)
