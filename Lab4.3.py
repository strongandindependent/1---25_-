def check_date(day, month, year):
    last_two = int(str(year)[-2:])
    if day * month == last_two:
        return True
    else:
        return False


day = int(input("День: "))
month = int(input("Месяц: "))
year = int(input("Год: "))

if check_date(day, month, year):
    print("True")
else:
    print("False")
