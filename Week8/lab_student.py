class LABStudent:
    # Constructor method
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    #name: str # attribuutti
    #age: int # attribuutti
    #major: str # attribuutti

    def introduce(self): # Metodi
        return f"Hi, I'm {self.name}, {self.age} years old, majoring in {self.major}"
    
    def study(self): # Method
        return f"{self.name} is sudying {self.major}."