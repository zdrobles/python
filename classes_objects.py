class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_school(self, school):
        self.school = school

    def get_school(self):
        return self.school

    def random(self):
        print("My name is", self.name)
        print("My age is", self.age)


demo_person = Person("Zach", 24)
demo_person.set_school("Kutztown")
print(demo_person.get_school())
demo_person2 = Person("Brie", 24)
demo_person.random()
