def verificaSeExiste(n):
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

print(verificaSeExiste(5))