a, b = input(), input()
colors = ['красный', 'синий', 'желтый']
if a not in colors or b not in colors:
    print('ошибка!')
elif a == "синий" and b == "желтый":
    print("зеленый")
elif a == "синий" and b == "красный":
    print("фиолетовый")
elif a == "желтый" and b == "красный":
    print("оранжевый")
elif a == "красный" and b == "желтый":
    print("оранжевый")
elif a == "желтый" and b == "синий":
    print("зеленый")
elif a == "красный" and b == "синий":
    print("фиолетовый")