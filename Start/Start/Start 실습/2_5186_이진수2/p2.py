
def binary(n):
    if n//2 == 0:
        return str(n%2)
    return binary(n//2)+str(n%2)
n = int(input())
print(binary(n), type(binary(n)))
