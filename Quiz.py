score = 0
name = input("Hvad er dit navn?")
print("velkommen til denne quiz!", name,  ". Du svarer ved at bruge tallene 1-3")

answer = input("Hvad er hovedstaden i Norge? - er det Oslo, Bergen eller Stavanger?")
answer = int(answer)

if answer == 1:
    print("Oslo er det rigtige svar!!!")
    score += 1

else:
    print("forkert svar")
    score -= 1

answer = input("Hvad er hovedstaden i Somalia? - er det Kismaayo, Mogadisho eller Somaliland?")
answer = int(answer)

if answer == 2:
    print("Mogadisho er det rigtige svar!!!")
    score += 1

else:
    print("forkert svar")
    score -= 1

answer = input("Hvad er hovedstaden i Danmark? - er det Odense, Aalborg eller København?")
answer = int(answer)

if answer == 3:
    print("København er det rigtige svar!!!")
    score += 1

else:
    print("forkert svar")
    score -= 1

answer = input("Hvad er hovedstaden i USA? - er det Texas, New York eller Washington D.C?")
answer = int(answer)

if answer == 3:
    print("Washington D.C er det rigtige svar!!!")
    score += 1

else:
    print("forkert svar")
    score -= 1

answer = input("Hvad er hovedstaden i Spanien? - er det Madrid, Barcelona eller Mallorca?")
answer = int(answer)

if answer == 1:
    print("Madrid er det rigtige svar!!!")
    score += 1

else:
    print("forkert svar")
    score -= 1

print(name, "your score is:", score)