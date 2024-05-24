def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    if len(ticket_str) % 2 != 0:
        return False

    half_length = len(ticket_str) // 2
    first_half = sum(int(digit) for digit in ticket_str[:half_length])
    second_half = sum(int(digit) for digit in ticket_str[half_length:])

    return first_half == second_half


ticket_number = input("Номер билета: ")
if lucky_ticket(ticket_number):
    print("Счастливый!")
else:
    print("Не счастливый(")
