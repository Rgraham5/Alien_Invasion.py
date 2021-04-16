import unittest
from alien_invasion import Alien
from settings import Settings

class testCase(unittest.TestCase):
	def testshipspeed(self):
		x = self.intialize_dynamic_settings()
		self.ship.speed = 1.5
		self.assertIn(self, x, 1.5)
if __name__ == '__main__':
    unittest.main()