class Person1:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am a {self.gender}.")
    
class Person2:
    def __init__(self, name, age, gender):
         self.name = name
         self.age = age
         self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am a {self.gender}.")

Person1_instance = Person1(name="George", age=21, gender="Male")
Person2_instance = Person2(name="Linda", age=21, gender="Female")

Person1_instance.introduce()
Person2_instance.introduce()
