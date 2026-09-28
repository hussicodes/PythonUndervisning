brugernavne = ["admin", "1234", "bruger1", "kode123"]
adgangskoder = ["1234", "kode123", "test123", "hemmelig"]

tries = 3

while tries != 0:
    print("Skriv dit brugernavn!")

    svar = input("")
    if svar in brugernavne:
        indeks = brugernavne.index(svar)
        print("skriv dit kodeord")
        svar = input("")
        if svar in adgangskoder[indeks]:
            print("Velkommen")

            print()
            print("Du har nu 4 valgmuligheder:" \
            "1. ændre brugernavne")
            svar = input("")


            if svar == "1":
                print("Skriv hvad du vil ændre", brugernavne[indeks], "til?")
                svar = input("")

                if svar in brugernavne:
                    print("Brugeren eksistere allerede!")

                else:
                    brugernavne[indeks] = svar
                    print("Du har ændret dit brugernavn til:")
                    print(brugernavne[indeks])

        else:
            tries -= 1
            print("Du tastede forkeret")
            print("du har ", tries, " tilbage")

    else:
        tries -= 1
        print("Du tastede forkeret")
        print("du har ", tries, " tilbage")
        print()