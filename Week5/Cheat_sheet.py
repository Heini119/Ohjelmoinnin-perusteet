# print() # on funktiokutsu
# print("Hello") # "Hello" on funktion parametri
# len() # on myös funktiokutsu, mitattava asia sisään



# while True:
#    print("I can do this forever") #tämä on koodiblokki

def greet(name):
    print(f"Hello {name}") #tässä on luotu funktio greet()

greet("Heini")
name = Heini
greet(name)

def greet(name):
    return f"Hello, {name}"

print(greet("Heini"))

def greeting_airport(person, age):
    print(f"How do you do {person}")
    if age >= 18:
        print("Welcome to your flight!")
    else:
        print(f"You need to wait for {18-age} years to fly solo.")

greeting_airport("Heini", 46)
TAI
greeting_airport(age=46, person="Heini")

Tee ohjelma, joka kysyy käyttäjältä kokonaislukua. Testaa funktiolla, onko se alkuluku vai ei.
Kysy uutta lukua, kunnes käyttäjä pyytää lopettamaan kysymisen.
