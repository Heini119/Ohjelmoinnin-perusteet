#Numero = int(input("Anna jokin numero: "))
#if Numero % 2 == 0:
#    print("Numero on parillinen")
#else:
#    print("Numero on pariton")


#Temp = int(input)"What is the tempersture of CPU? "
#if(Temp > 80):
 #   if(Temp > 90):
 #       print("You are toast")
 #   else:
 #       print("Warning!")

#else:
#    print("You are OK")

#Name1 = input("Anna nimi: ")
#Name2 = input("Anna toinen nimi: ")
#if len(Name1) > len(Name2):
#    print("Ensimmäinen nimi on pidempi")
#elif len(Name1) < len(Name2):
#    print("Toinen on pidempi")
#else:
#    print("Yhtä pitkät")

#Town = "Lahti"
#Street = "Mukkulankatu" \
#Building = 19

#if(Town == ("Lahti" or "Lahtis") and Street == "Mukkulankatu" and Building == 19):
#    print("You are at LAB")
#elif(Town == "Lahti" and (Street != "Mukkulankatu" or Building != 19)):
#    print("You are in the correct town but check the street address again")
#elif not(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
#    print("You are completely lost...")

#import random

#print(random.random())
#print(random.randint(1,6))

import random

choices = ["kivi", "paperi", "sakset"]

computer_choice = random.choice(choices)

player_choice = input("Valitse kivi, paperi tai sakset")

print(f"Pelaaja valitsi: {player_choice}")
print(f"Tietokone valitsi: {computer_choice}")







