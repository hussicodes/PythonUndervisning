print("Velkommen til parkeringssystemet")
parkeringspladser = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    print("\nVælg 1 for at se antal ledige pladser.")
    print("Vælg 2 for at booke en plads.")
    print("Vælg 3 for at afslutte programmet.")
    
    svar = input("Indtast dit valg: ")
    
    if svar == "1":
        if len(parkeringspladser) > 0:
            print("Ledige pladser:", parkeringspladser)
        else:
            print("Der er desværre ingen ledige pladser.")

    elif svar == "2":
        print("Ledige pladser:", parkeringspladser)
        valg_plads = int(input("Hvilken plads vil du booke? "))
        
        if valg_plads in parkeringspladser:
            parkeringspladser.remove(valg_plads)
            print(f"Du har succesfuldt booket plads nummer {valg_plads}!")
        else:
            print("Ugyldig plads eller pladsen er allerede optaget.")

    elif svar == "3":
        print("Forlader parkeringssystemet...")
        break
 
    else:
        print("Forkert input, prøv igen.")