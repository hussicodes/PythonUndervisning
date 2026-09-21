print("Hej! Velkommen.")

while True:
    tal1 = float(input("skriv det første tal "))
    tal2 = float(input("skriv det andet tal "))

    math = input("her skriver du endten + - * eller /")


    if(math == "+"):
        mathPlus = tal1 + tal2
        print(mathPlus)
        

    elif(math == "-"):
        mathMinus = tal1 - tal2
        print(mathMinus)
        

    elif(math == "*"):
        mathGange = tal1 * tal2
        print(mathGange)

    elif(math == "/"):
        mathDivider = tal1 / tal2
        print(mathDivider)
        
    else:
        print("Du skal skrive en matematisk operatorer (+-*/)")
    print("Vildu gerne regne igen?")
    svar = input("Ja eller nej?")
    if svar == "nej":
        break