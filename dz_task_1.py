# ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def generate(n):
    cnt = 0
    for i in range(2, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 2:
            yield i
        else:
            cnt = 0
result = generate(100) 

for i in result:
    print(i)
