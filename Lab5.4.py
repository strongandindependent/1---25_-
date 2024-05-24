a = ['ф','а','с','к','х','ы']
b = ['п','я','д','ж','и']
concatenated_tuple = a[1:3] + b[3:4]
all = a + b + concatenated_tuple
print(concatenated_tuple)
print(all)
print(len(all))
all.sort()
print(all)
if "а" in all:
    times = all.count("а")
    print("'a' is found in the list", times)
else:
    print("'John' is not found in the list")

