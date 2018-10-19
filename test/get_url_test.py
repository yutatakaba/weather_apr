import unittest
from get_url import GetUrl


class TestGetUrl(unittest.TestCase):
	def setUp(self):
		self.get_url = GetUrl()

	def test_get_area_num(self):
		self.assertEqual(1, self.get_url.get_area_num("北海道"))
		self.assertEqual(2, self.get_url.get_area_num("東北"))
		self.assertEqual(3, self.get_url.get_area_num("関東"))
		self.assertEqual(4, self.get_url.get_area_num("信越・北陸"))
		self.assertEqual(5, self.get_url.get_area_num("東海"))
		self.assertEqual(6, self.get_url.get_area_num("近畿"))
		self.assertEqual(7, self.get_url.get_area_num("中国"))
		self.assertEqual(8, self.get_url.get_area_num("四国"))
		self.assertEqual(9, self.get_url.get_area_num("九州"))
		self.assertEqual(10, self.get_url.get_area_num("沖縄"))

	def test_get_url(self):
		self.assertEqual("http://weather.livedoor.com/area/1", self.get_url.get_url("北海道"))
		self.assertEqual("http://weather.livedoor.com/area/2", self.get_url.get_url("東北"))
		self.assertEqual("http://weather.livedoor.com/area/3", self.get_url.get_url("関東"))
		self.assertEqual("http://weather.livedoor.com/area/4", self.get_url.get_url("信越・北陸"))
		self.assertEqual("http://weather.livedoor.com/area/5", self.get_url.get_url("東海"))
		self.assertEqual("http://weather.livedoor.com/area/6", self.get_url.get_url("近畿"))
		self.assertEqual("http://weather.livedoor.com/area/7", self.get_url.get_url("中国"))
		self.assertEqual("http://weather.livedoor.com/area/8", self.get_url.get_url("四国"))
		self.assertEqual("http://weather.livedoor.com/area/9", self.get_url.get_url("九州"))
		self.assertEqual("http://weather.livedoor.com/area/10", self.get_url.get_url("沖縄"))

	def test_get_url_error(self):
		self.assertEqual(None, self.get_url.get_url("神奈川"))


if __name__ == "__main__":
	unittest.main()
