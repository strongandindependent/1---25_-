char_list = []
string = input()
for c in string:
    char_list.append(c)
if 'ф' in char_list:
    print('Redkoye')
else:
    print('Ne redkoye')