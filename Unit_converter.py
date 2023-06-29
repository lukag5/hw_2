print("Hello user! In this case you have possibility to convert km into miles: ")

while True:
    km = float(input("Please enter a number of kilometers: "))
    miles = float(km*0.621371192)
    print(str(miles) + " " + "miles")
    question = input("If you want to do another conversion, press Y or N: ")
    if question == "Y":
        pass
    else:
        break

print("Goodbye")