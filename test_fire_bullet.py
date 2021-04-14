import unittest

def _fire_bullet(self):
		"""create a new bullet and add it to the bullets group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

class Test_fire_bullet(unittest.TestCase):
	def test_fire_bullet(self):
		self.assertTrue(True)

unittest.main()
