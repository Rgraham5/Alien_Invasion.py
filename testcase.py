import unittest
from alien_invasion import Alien

class testCase(unittest.TestCase):
	def test_fire_bullets(self):
		#arrange
		#Act
		X = len(self.bullets) < self.settings.bullets_allowed
		Y = self.bullets.add(new_bullet)
		msg = none
		#assert
		self.assertIn(self, bullets, msg)



	#if len(self.bullets) < self.settings.bullets_allowed:
	#		new_bullet = Bullet(self)
	#		self.bullets.add(new_bullet)


if __name__ == '__main__':
    unittest.main()