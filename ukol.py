predmety = ["Dějepis", "Fyzika", "Přírodopis", "Tělocvik", "Chemie", "Anglický jazyk"]
print(len(predmety))
for i in predmety:
    print(i)
    dalsi_predmet = input("Zadejte další předmět: ")
    predmet.append(dalsi_predmet)
    print(predmety)
    predmety.pop(0)
    predmety.sort(reverse=True)
    print(predmety)
    predmety.reverse()
    print(predmety)