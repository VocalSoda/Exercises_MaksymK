usrname = "python"
password = "rules"
tries = 0 
while True:
    a = str(input("please enter username: "))
    b = str(input("please enter password: "))
 
    if a != usrname and b != password:
        tries=tries+1
        print(f"Incorrect, remaining amount of tries is {5-tries}")
        if tries == 5:
            print("access denied")
            break
    else:
        print("welcome")
        break