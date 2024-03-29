class Person:
    def introduce(self):
        return person1.name  
    def introduce1(self):
        return person1.age
    def introduce2(self):
        return person1.gender

person1 = Person()
person1.name = "Francis"
person1.age = 23
person1.gender = "male"
#print("Hi my name is", person1.name, "Iam a", person1.age, "year old", person1.gender)
#     def __init__(self, name,  age , gender) -> None:
#         self.name = name
#         self.age = age 
#         self.gender = gender

# person1 = Person("Francis",  23, "male")

# print("Hi, my name is " person1.name ", Iam " person1.age "years old. I am a" person1.gender".")

print("This is", person1.introduce(), 'He is a',  person1.introduce1(), "year old", person1.introduce2() )