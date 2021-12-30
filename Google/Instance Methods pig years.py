class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
print(hamlet.pig_years())
hamlet.years = 2
print(hamlet.pig_years())


class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())