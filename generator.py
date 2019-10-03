def fibonacchi(a0, a1, n):
    yield a0
    yield a1
    i = 2
    while i < n:
        yield a0 + a1
        a0, a1 = a1, a0 + a1
        i += 1
        
for x in fibonacci(1, 1, 10):
    print(x)
