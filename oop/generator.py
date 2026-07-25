def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

for n in even_numbers(10):
    print(n, end=" ")
