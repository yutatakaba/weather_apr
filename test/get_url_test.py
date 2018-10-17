import unittest
from get_url import GetUrl


class TestGetUrl(unittest.TestCase):
	def setUp(self):
		self.get_url = GetUrl()

	def test_get_url(self):
		self.assertEqual(True, self.get_url.get_url())


if __name__ == "__main__":
	unittest.main()
