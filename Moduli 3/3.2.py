# customer = input("Please enter your cabin class, either LUX, A, B or C: ")

# if customer == "LUX":
#     print("upper-deck cabin with a balcony")
# elif customer == "A":
#     print("above the car deck, equipped with a window")
# elif customer == "B":
#     print("windowless cabin above the car deck")
# elif customer == "C":
#     print("windowless cabin below the car deck")
# else:
#     print("Please for the love of god choose one of the listed options.")


cus = input("Please enter your class: ") 
res = (print("upper-deck cabin with a balcony") if cus == "LUX" else print("above the car deck, equipped with a window") if cus == "A" else print("above the car deck, equipped with a window") if cus == "B" else print("windowless cabin above the car deck") if cus == "C" else print("Please for the love of god choose one of the listed options."))
res
