hght = int(input("Your height: "))

if hght > 195:
     print("liian pitka")
else:
    if hght > 140:
        print("saa menna kaikkiin laitteisiin")
    elif hght > 100:
        print("saa menna lasten laitteisiin")
    else:
        print("ei saa menna")