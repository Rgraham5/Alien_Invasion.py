import unittest
from alien_invasion import AlienInvasion


class testAlien(unittest.TestCase):

	def test_alien(self):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)	

		self.assertIn(self, alien.x)

if __name__ == '__main__':
    unittest.main()