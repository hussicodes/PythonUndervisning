print("velkommen til butikken!")
print("")
varer = ["Cola", "Brød", "Smør", "Mælk", "Æg", "Chips", "Kød", "Tomater", "Æbler", "Agurk"]
varerPris = [5, 10, 20, 15, 23, 25, 100, 13, 21, 16]
kurv = True

while kurv == True:
    print("Her under er der varer du kan købe")
    for vare in varer:
        print(vare, end=', ')