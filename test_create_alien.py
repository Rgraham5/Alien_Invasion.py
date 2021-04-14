import unittest


def _create_alien(self, alien_number, row_number):
	"""create an alien and place it in the row."""	
	alien = Alien(self)
	alien_width, alien_height = alien.rect.size
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	self.aliens.add(alien)	

Class Test_create_alien(unittest.TestCase):
	def test_create_alien(self):
		self.assertTrue(True)