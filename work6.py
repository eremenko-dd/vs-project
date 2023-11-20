"""
игра с поиском зверушек за окном.
Давайте поиграем и найдём заек.

Формат ввода
В первой строке записано натуральное число N — количество выделенных придорожных местностей.
В каждой из N последующих строк записано описание придорожной местности.

Формат вывода
Количество заек.
"""
count = 0
for i in range(int(input())):
    text = input()
    count += text.count('зайка')
print(count)
"""
Пример 
Ввод
3
березка елочка зайка волк березка
сосна зайка сосна елочка зайка медведь
сосна сосна сосна белочка сосна белочка

Вывод
3
"""