class Car:
    def __init__(self,color,brandName,Speed):
        self.color = color
        self.brandName = brandName
        self.Speed = Speed

    def details(self):
        print(self.color,self.brandName,self.Speed)

Audi = Car("Black","Audi","150")
Audi.details()

Porcshe = Car("White","Porcshe","200")
Porcshe.details()
print(Porcshe.color)

