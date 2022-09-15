import sys

sys.stdin = open('input.txt')


def inorder(n):
    global stack
    if n:
        inorder(ch1[n])
        result.append(tree[n])
        inorder(ch2[n])
        if type(tree[n]) == int:
            stack += [tree[n]]
        else:
            a = stack.pop()
            b = stack.pop()
            if tree[n] == '+':
                stack += [b+a]
            elif tree[n] == '-':
                stack += [b-a]
            elif tree[n] == '*':
                stack += [b*a]
            elif tree[n] == '/':
                stack += [b/a]
for _ in range(10):
    n = int(input())
    tree = [0] * (n + 1)  # 정점 값 저장
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)

    result = []
    for i in range(n):
        arr = list(map(str, input().split()))
        V = int(arr[0])
        if len(arr) == 4:
            tree[V] = arr[1]
            ch1[V] = int(arr[2])
            ch2[V] = int(arr[3])
        elif len(arr) == 2:
            tree[V] = int(arr[1])
    stack= []
    inorder(1)

    print(int(stack[0]))