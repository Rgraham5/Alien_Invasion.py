import unittest

def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""
		#Update bullet positions.
		# Get rid of bullets that have disappeared.
		self.bullets.update()


		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				 self.bullets.remove(bullet)
		
		self._check_bullet_alien_collisions()

class Test_update_bullets(unittest.TestCase):
	def test_update_bullets(self):
		self.assertEqual()

unittest.run()