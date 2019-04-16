class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    
    self.venom = 100

    def __init__(self):
	"""Initialize that Cobra"""
        self.venom=300
	

    def bite(self, other):
        """Deliver a dose of venom."""
        other.bitten = True
	self.venom = self.venom - 10
	print("That bites!")
	return
    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        from bear import hug
        hug(self, other, kill=True)

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""

    def __init__(self):
        """Create a new BoatConstrictor"""
        super().__init__()
        self.size = "enormous"
