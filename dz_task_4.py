 # Создайте функцию генератор чисел Фибоначчи (см. Википедию).
NUMBER = 10

def fib(n):
    a = b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for i in fib(NUMBER):
    print(i, end=' ')
print()
