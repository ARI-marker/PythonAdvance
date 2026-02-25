class Dog:
    def __int__(self , name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Ham")


class Cat:
    def __int__(self , name):
        self.name = name
    def sound(self):
        print(f"{self.name} makes the sound: Mijau")



class Bird:
    def __int__(self , name):
        self.name = name
    def sound(self):
        print(f"{self.name} makes the sound: ciu")



dog = Dog("Max")
cat = Cat("Oto")
bird = Bird("Chipo")


for animal in (dog , cat , bird):
    animal.sound()
        