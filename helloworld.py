def hello():
    return 'Hello World!'

print(hello())


def sum_all(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_all(n - 1)
    
print(sum_all(5))


def add(x, y):
    return x + y

print(add(5, 4))