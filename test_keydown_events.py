import unittest

def _check_keydown_events(self, event):
		"""Key presses"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

class Test_check_keydown_events(unittest.TestCase):
	def Test_check_keydown_events(self):
		self.assertTrue(self, event, True)

unittest.main()