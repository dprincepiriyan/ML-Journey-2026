class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)#calling the parent class constructor
        self.graduationyear=year
x=person("John","Doe")
y=student("mike","Doe","2024")
x.printname()
y.printname()
print(y.graduationyear)