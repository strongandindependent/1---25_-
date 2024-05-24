a = [0, 3, 0]
b = len(a)
for i in range(1, b):
    if a[i-1] == a[i]:
        print(a[i])
    else:
        print('NO')