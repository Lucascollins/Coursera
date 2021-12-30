class Animal:
    sound = ""
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.sound} I'm  {self.name}! {self.sound}")



class Piglet(Animal):
    sound = "Oink!"

class Cow(Animal):
    sound = "Moooo!"

class Cat(Animal):
    sound = "Miau!"

class Dog(Animal):
    sound = "Auau"



hamlet = Piglet("Hamlet")
hamlet.speak()

milky = Cow("Milky White")
milky.speak()

mingau = Cat("Mingau")
mingau.speak()

thor = Dog("Thor")
thor.speak()



class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()