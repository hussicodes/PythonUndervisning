print("Velkommen til butikken!")
print("")

varer = ["Cola", "Brød", "Smør", "Mælk", "Æg", "Chips", "Kød", "Tomater", "Æbler", "Agurk"]
varerPris = [5, 10, 20, 15, 23, 25, 100, 13, 21, 16]

# Ydre løkke til at holde systemet kørende til flere kunder
kassen_aaben = True

while kassen_aaben:
    kurv = []
    kurv_priser = []
    
    # Indre løkke til når kunden handler
    er_i_gang = True
    while er_i_gang:
        print("\nHer under er der varer du kan købe:")
        for vare in varer:
            print(vare, end=', ')
        print("\n")
        
        # Her stopper programmet og venter på, at du skriver noget!
        valg = input("Skriv navnet på en vare, skriv 'betal', eller skriv 'luk': ").strip().capitalize()
        
        # 1. Tjek om kunden vil betale
        if valg == "Betal":
            if len(kurv) == 0:
                print("Din kurv er tom!")
            else:
                print("\n--- KVITTERING ---")
                samlet_pris = 0
                
                # For-løkke til at gennemgå indkøbskurven
                for i in range(len(kurv)):
                    print(f"- {kurv[i]}: {kurv_priser[i]} kr.")
                    samlet_pris += kurv_priser[i]
                    
                print(f"Antal varer i alt: {len(kurv)}")
                print(f"Samlet pris: {samlet_pris} kr.")
                print("Tak for din handel!\n")
                
                # Afslut denne kundes tur, så næste kunde kan starte
                er_i_gang = False
                
        # 2. Tjek om kunden vil lukke kassen helt
        elif valg == "Luk":
            print("Selvbetjeningskassen lukkes. Farvel!")
            er_i_gang = False
            kassen_aaben = False
            
        # 3. Tjek om varen findes i vores vare-liste
        elif valg in varer:
            indeks = varer.index(valg)
            kurv.append(varer[indeks])
            kurv_priser.append(varerPris[indeks])
            print(f"-> Du har tilføjet {valg} ({varerPris[indeks]} kr.) til din kurv.")
            
        # 4. Hvis varen ikke findes eller skrives forkert
        else:
            print("Ugyldigt valg. Prøv at skrive navnet på varen præcist, f.eks. 'Cola'.")