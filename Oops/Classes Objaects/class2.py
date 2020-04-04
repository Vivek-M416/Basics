class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def last_name(self):
        print('Last name : ' + self.name)

    def first_name(self):
        print('FIrst name : ' + self.name.split(' ')[0])


S1 = Student('vivek Annamneni', 15, 529)

print(S1.first_name())
print(S1.last_name())
print(S1.marks)
