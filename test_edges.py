import unittest

def check_edges(self):
		"""Return True if alien is at the edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

class testcheck_edges(unittest.TestCase):
	def testcheck_edges(self):
		exp = self.screen.get_rect()
		self.assertTrue(exp, True)

if __name__ == '__main__':
    unittest.main()