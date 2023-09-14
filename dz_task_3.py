# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

NAME = ['Ivan', 'Kirill']
VALUE = [100, 200]
BONUS = ['10.25%', '20.50%']

# def my_func(name, value, bonus):
#     for i in range(len(name)):
#         print({name[i]:(int(value[i]/100)*float(bonus[i][:-1]))})
# my_func(NAME, VALUE, BONUS)
awards = {name: value * float(bonus[:-1]) / 100 for name, value, bonus in zip(NAME, VALUE, BONUS)}
print(awards)
