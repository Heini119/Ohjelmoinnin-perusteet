Children = 3
Hometown = "Pirkkala"

#Lista merkitään [] ja Dictionary {}

# Lista
TownsInFinland = ["Pirkkala", "Helsinki", "Oulu", "Tampere"]

RandomInformation = ["Heini", 46, True, Children, Hometown]

print(TownsInFinland[0]) #-> tulos Pirkkala
TownsInFinland.append("Rovaniemi") # -> listaan lisätään Rovaniemi

NumOfTowns = len(TownsInFinland) # -> vastaus on 6
print(TownsInFinland[NumOfTowns-1]) # -> Rovaniemi, koska lukumäärä on 0,1,2,3,4,5

Municipalities = ["Nokia", "Vesilahti", "Kangasala", "Lempäälä"]
Towns = ["Pirkkala", "Helsinki", "Oulu", "Tampere"]

MunicipalitiesAndTowns = [Municipalities, Towns]
print(MunicipalitiesAndTowns [1][-2]) #eka[] kertoo, kumpi lista valitaan, [-2] kertoo kuinka mones listasta

Towns.sort()
print(Towns) # -> aakkosjärjestyksessä, koska Towns.sort

Teacher = (
    'name': 'Juha',
    'age': 50,
    'city': 'Lahti'
)

print(Teacher['name'])

Teacher['email']: juha.hyytiainen@lab.fi

print(Teacher) #Tuo dictionaryyn syötetyt tiedot muuttujalle Teacher

for key in Teacher:
    print(key, end=" ")
    print(Teacher[key])

Student = [
    {'name': 'Mikko', 'age': 25, 'city': 'Tampere'},
    {'name': 'Maija', 'age': 20, 'city': 'Oulu'},
    {'name': 'Seppo', 'age': 45, 'city': 'Lahti'}
]

Print(Student[0]) #-> antaa Mikon tiedot

Cities = {
    'Finland':['Tampere', 'Espoo', 'Helsinki'],
    'Sweden':['Stockholm', 'Malmö']
}

print(Cities['Finland'][0]) #-> Tulos Suomi-listan ensimmäinen eli Tampere

for town in Towns:
    print(f"The town of {town}") #-> printtaa listan "The town of Lahti jne."
print(f"All of the towns {Towns}") #-> printtaa kaikki kaupungit

for i in range(1,10): 
    print(i) #printtaa nrot 1-9, jokaisen omalle rivilleen

for i in range(1, 10):
    print(i, end=" ") #printtaa samalle riville nrot 1-9
for i in range(1, 10, 3):
    print(i) #printtaa 1-9, kolmen askelen välein

Total = 0
for i in range(1,101):
    Total +=i
    print(Total) #lisää joka kierroksella summaan kierrosluvun (1,3,6,10,15 jne.)

for i in range(9):
    if (i == 3):
        continue
    print(i) #printtaa kaikki paitsi kolmannen kierroksen, koska continue jatkaa toimintaa

# opiskele for ja while -loopit, sekä niihin liittyvät komennot break ja continue

while 1 < 10:
 #   print("Do not try me at home xD") # ikuinen looppi

i = 0
while i < 10:
    print(f"Iteration number: {i}")
    i += 1
    # (i = i + 1)

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") != "yes":
        continueLoop = False # niin pitkään kuin vastataan "yes", kysyy uudestaan - jos vastaa jotain muuta, lopettaa

while True:
    if input("Do you want to continue? ") != "yes":
        break
    else:
        continue

