liv = 100               
ressourcer = 10.5       
spiller_navn = ""       
spil_igang = True       

print("Velkommen til tekst-eventyret!")
spiller_navn = input("Indtast dit navn: ")

while spil_igang and liv > 0:
    print(f"\n--- Status: {spiller_navn} | Liv: {liv} | Ressourcer: {ressourcer} ---")
    print("1. Gå ind i den mørke skov")
    print("2. Gå ind i grotten")
    print("3. Afslut spillet")
    
    valg = input("Vælg en handling (1-3): ")

    if valg == "1":
        print("Du går ind i skoven og rammer en fælde!")
        liv -= 5  
        ressourcer += 2.0
        
    elif valg == "2":
        print("Du finder en låst kiste i grotten.")
        
        laast = True
        while laast and liv > 0:
            gaet = input("Gæt koden (et tal mellem 1 og 3): ")
            
            if gaet == "2":
                print("Kisten åbnede sig! Du fik 10 ressourcer.")
                ressourcer += 10.0
                laast = False  
            else:
                print("Forkert kode! Det tærer på kræfterne.")
                liv -= 2  
                if liv <= 0:
                    break
                    
    elif valg == "3":
        print("Du valgte at opgive. Farvel!")
        spil_igang = False
        
    else:
        print("Ugyldigt valg, prøv igen.")

    if liv <= 0:
        print("\nDu har mistet alt dit liv. Du er DØD! Game Over.")
        spil_igang = False