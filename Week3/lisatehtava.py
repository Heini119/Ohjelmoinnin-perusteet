Tunnus = input("Anna käyttäjätunnus: ")
Ikä = int(input("Anna ikäsi: "))
Admin = input("Oletko admin (K/E): ")
print()
if Tunnus == "Heini" and Ikä >= 18 and Admin == "K":
    print("Pääsy sallittu.")
elif Tunnus == "Heini" and Ikä >= 18 and Admin == "E":
    print("")



