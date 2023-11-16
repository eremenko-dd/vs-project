foo = True
for i in range(int(input())):
    text = input()
    if text[0].lower() not in ("а","б","в"):
        foo = False
print('YES' if foo else "NO")
"""
Программа проверяет заданное количество введённых слов, начинаются ли они на "а","б","в" или нет
"""