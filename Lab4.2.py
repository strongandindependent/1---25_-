def hundred_divisio_on(x):
    try:
        return 100 / x
    except ZeroDivisionError:
        print('Ошибка! Деление на 0')
    except ValueError:
        print("Не число!")


print(hundred_divisio_on(int(input())))