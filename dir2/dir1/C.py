def gen(n):
    for i in range(n):
        if i%2 == 0:
            yield 1
        else:
            yield -1

N = [i for i in gen(4)]
print(N)
