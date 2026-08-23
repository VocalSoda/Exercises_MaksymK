while True:
      gender = input("Male or Female?: ").strip().capitalize()
      if gender in ["Male", "Female"]:
        break
      else:
          print("Please type in either Male or Female")

while True:
    try:
        hemo = int(input("Hemoglobin value?: "))
        break
    except ValueError:
        print("Hemoglobin should be an integer")



match gender:
    case "Male":
        if hemo > 134 and hemo < 167:
            print("Hemoglobin is normal")
        elif hemo < 134:
             print("Hemoglobin is quite low")
        else:
            print("Hemoglobin is quite high")

    case "Female":
        if hemo > 117 and hemo < 155:
            print("Hemoglobin is normal")
        elif hemo < 117:
            print("Hemoglobin is quite low")
        else:
            print("Hemoglobin is quite high")


