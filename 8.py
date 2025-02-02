class Animal:
    def speak():
        pass
class Dog(Animal):
    def speak(self):
        print('Bow Bow')
class Cat(Animal):
    def speak(self):
        print('MeowMeow')
d=Dog()
d.speak()
c=Cat()
c.speak()