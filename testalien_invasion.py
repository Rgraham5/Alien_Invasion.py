import unittest
from alien_invasion import AlienInvasion

class TestAlienInvasion(unittest.TestCase):

	def setUp(self):
		pass
	
	def tearDown(self):
		pass
	
	def Test_check_keydown_events1(self):
		#if event.key == pygame.K_RIGHT:
			#self.ship.moving_right = True
		# Arrange
		# Act
		# Assert
		self.assertTrue(self, event, True)

	def Test_check_keydown_events2(self):
		#elif event.key == pygame.K_LEFT:
			#self.ship.moving_left = True
		#arrange
		#act
		#assert
		self.assertTrue(self, event, True)

	def test_check_keyup_events1(self):
		#testing K_q
		# Arrange
		actual = K_q
		# Act
		result = sys.exit()
		# Assert
		self.assertTrue(self, event)

	def test_check_keyup_events2(self):
		# Arrange
		#elif event.key == pygame.K_LEFT:
		#	self.ship.moving_left = False 
		# Act
		# Assert
		self.assertFalse(self, event)

	
#or

	def test_check_keyup_events3(self):
		#if event.key == pygame.K_RIGHT:
		#	self.ship.moving_right = False
		#elif event.key == pygame.K_LEFT:
		#	self.ship.moving_left = False 
		# Arrange
		
		# Act
		
		# Assert
		self.assetFalse(self, event) or self.assertEqual(K_LEFT, K_RIGHT)

	

if __name__ == '__main__':
    unittest.main()

   #def _check_keydown_events(self, event):
		"""Key presses"""
		#if event.key == pygame.K_RIGHT:
			#self.ship.moving_right = True
		#elif event.key == pygame.K_LEFT:
			#self.ship.moving_left = True
		#elif event.key == pygame.K_q:
			#sys.exit()
		#elif event.key == pygame.K_SPACE:
		#	self._fire_bullet()

	#def _check_keyup_events(self, event):
		"""key releases"""
		#if event.key == pygame.K_RIGHT:
		#	self.ship.moving_right = False
		#elif event.key == pygame.K_LEFT:
		#	self.ship.moving_left = False 

	#def _fire_bullet(self):
		"""create a new bullet and add it to the bullets group"""
	#	if len(self.bullets) < self.settings.bullets_allowed:
	#		new_bullet = Bullet(self)
	#		self.bullets.add(new_bullet)

	#def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""
		#Update bullet positions.
		# Get rid of bullets that have disappeared.
	#	self.bullets.update()


	#	for bullet in self.bullets.copy():
	#		if bullet.rect.bottom <= 0:
	#			 self.bullets.remove(bullet)
		
	#	self._check_bullet_alien_collisions()


	#def _create_alien(self, alien_number, row_number):
		"""create an alien and place it in the row."""	
		#alien = Alien(self)
		#alien_width, alien_height = alien.rect.size
		#alien.x = alien_width + 2 * alien_width * alien_number
		#alien.rect.x = alien.x
		#alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		#self.aliens.add(alien)	