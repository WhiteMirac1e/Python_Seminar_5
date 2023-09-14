# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def row(path):
    *path_e, name_ext = path.split('/')
    name, extension = name_ext.split('.')
    return '/'.join(path_e) + '/', name, extension

path = '/test/fort/123/t34.txt'

print(row(path))
