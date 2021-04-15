import unittest
from alien_invasion import Alien
from bullet import Bullet

"""def draw_bullet(self):
		Draw the bullet to the screen.
		pygame.draw.rect(self.screen, self.color, self.rect)""" 

class TestCase(unittest.TestCase):
	#test that bullet class is in alien invasion class
	def test_bullet(self):
		self.bullet()
		self.assertIn(Alien, Bullet)

if __name__ == '__main__':
    unittest.main()
