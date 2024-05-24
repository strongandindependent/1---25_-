a = [1, 2, 3, 4, 5, 6, 7]
weeks = int(input())
b = a[-weeks:]
print(b)
del a[-weeks:]
print(a)