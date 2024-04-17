class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print("Meow0")

    def displayinfo(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')

class DomesticCat(cat):
        def __init__(self,cat,age,ownwer, homeaddress):
             super().__init__(cat, age)
             self.owner = ownwer
             self.homeaddress = homeaddress

cat1 = DomesticCat('Simu', 20 , 'dhesi chai','takanini')
cat1.displayinfo()

# class WildCat(Cat):
     