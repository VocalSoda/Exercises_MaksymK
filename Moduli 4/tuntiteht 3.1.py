while True:
    try:
        luku = int(input("Anna luku: "))
        break
    except ValueError:
        print("Give number!")

if luku == 2020:
    print("Its korona time, it was in 2021")
elif luku % 4 == 0:
    print("Olympiavuosi!")

else:
    print("Ei ollut olympiavuosi")