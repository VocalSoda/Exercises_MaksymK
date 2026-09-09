month_tuple = ("spring", "summer", "autumn", "winter")
usr_input = int(input("Please provide number of the month 1-12: "))
if usr_input <= 2 or usr_input == 12:
    print(month_tuple[3])
elif usr_input > 2 and usr_input < 6:
    print(month_tuple[0])
elif usr_input > 5 and usr_input < 9:
    print(month_tuple[1])
else:
    print(month_tuple[2])