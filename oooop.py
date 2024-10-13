class Student:
    def sushant(self, name, age, classs):
        self.name = name
        self.age = age
        self.classs = classs
a = Student()

a.sushant("sushANT",12,"OK")

print(a.name)
print(a.age)
print(a.classs)


b = Student()

b.sushant("prajot",22,"ooook")

d = (b.name,b.age,b.classs)
print(d)
print(type(d))
d = list(d)
print(type(d))
print(d)
d[1]= 80

print(d)