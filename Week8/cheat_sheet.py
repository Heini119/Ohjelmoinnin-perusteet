#import pandas as pd
#import matplotlib.pyplot as plt

#data = {
#    'Temperature': [23, 22, 12, 32, 14, 20, 22, 22, 22, 21],
#    'Movement': [1, 0, 1, 1, 1, 1, 0, 0, 0, 1]
#}

#Luo dataframe
#df = pd.DataFrame(data)
#print(df)

#Piirrä kaavio
#plt.figure(figsize=(10,5))
#fig, ax = plt.subplots(2, 1)
#ax[0].plot(df['Temperature'], label="Temperature over time")
#plt.xlabel('Time')
#plt.ylabel('Value')
#ax[1].plot(df['Movement'], label="Movement over time")
#plt.xlabel('Time')
#plt.ylabel('Value')
#plt.legend()
#plt.show()

#import turtle

#sipi = turtle.Turtle() # Luo uusi kilpikonna-olio eli Turtle-instanssi
#sipi.shape("turtle") # Metodi
#sipi.color("green") # Metodi
#sipi.forward(100) # Metodi

#turtle_screen = turtle.Screen() # Luo uusi ikkuna-olio eli instanssi
#turtle_screen.exitonclick() # Metodi

########################################################3

#class LABStudent:
#    name: str # attribuutti
#    age: int # attribuutti
#    major: str # attribuutti

#    def introduce(self): # Metodi
#        return f"Hi, I'm {self.name}, {self.age} years old, majoring in {self.major}"
    
#    def study(self): # Method
#        return f"{self.name} is sudying {self.major}."

#John = LABStudent()
#John.name = "John"
#John.age = 32
#John.major = "Computer science"

#Jane = LABStudent()
#Jane.name = "Jane"
#Jane.age = 45
#Jane.major = "Physics"

#print(John.introduce())
#print(Jane.study())

######################################3

from lab_student import LABStudent

John = LABStudent("John", 32, "Computer science")
Jane = LABStudent("Jane", 45, "Physics")


print(John.introduce())
print(Jane.study())