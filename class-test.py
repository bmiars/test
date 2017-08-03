import random
class Thief:
	sneaky = True

	def pick_pocket(self):
		if self.sneaky():
			return bool(random.randint(0,1))
		return False

		
