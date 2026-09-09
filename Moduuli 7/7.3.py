airport_dict = {
    "EGLL":"London Heathrow Airport",
    "LFPG":"Charles de Gaulle International Airport",
    "EFHK":" Helsinki-Vantaa Airport"
}


while True:
    usr_input = input("Fetch airport press a , create new n, quit q : ")
    
    if usr_input == "n":
        airport_icao = input("Please enter icao of the airport: ")
        airport_name = input("please enter airport name: ")
        airport_dict.update({airport_icao:airport_name})
    elif usr_input == "a":
        fetch_icao = input("please provide airport ICAO code: ")
        try:
            print(airport_dict[fetch_icao])
        except:
            print("Nothing found")
            
    elif usr_input == "q":
        break