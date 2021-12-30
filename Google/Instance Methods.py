class Piglet:
    name = "piglet"
    def speak(self):
        print(f"Oink! i'm {self.name} ! Oink")

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()
