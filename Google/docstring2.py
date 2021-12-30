class Piglet:
    """Represents a piglet that can say their name."""
    years = 0
    name =""
    def speak(self):
        """Outputs a message incluiding the name of the piglet."""
        print(f"Oinl! I'm {self.name}! Oink!")
    def pig_years(self):
        """Converts the current age  to equivalent pig years."""
        return self.years * 18