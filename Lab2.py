def F(x):
    if x % 4 == 0 and x % 100 != 0:
        return ('Год', x, 'високосный')
    else:
        return ("Год не високосный")


i = int(input())
print(F(i))