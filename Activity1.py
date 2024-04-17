class person:
    def __init__(self, name, age, haircolor, eyecolor):
        self.name = name
        self.age = age
        self.haircolor = haircolor
        self.eyecolor = eyecolor
        self.hasbeard = True

    def speaks(self, quote):
      
      
        print(f"{self.name} says:", quote)

    def gets_older(self, years):
        self.age += years
        print(f"{self.name} is now {self.age}")

    def ishairy(self):
        if self.hasbeard == True:
            print(f"{self.name} has a cool beard.")
        else:
            print(f"{self.name} has a cool chin.")


cindy = person ("cindy shaw" , 44 , "blonde" , "brown")
henry = person("henry", 34, "brown", "blue")
cindy.speaks("yahoo")
henry.gets_older(6)
cindy.ishairy()
print(cindy.name)
print(henry.age)