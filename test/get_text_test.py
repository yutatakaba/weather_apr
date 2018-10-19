import unittest
from get_text import GetText


class TestGetText(unittest.TestCase):
	def setUp(self):
		self.get_text_kan = GetText("関東")
		self.get_text_err = GetText("神奈川")

	def test_get__url(self):
		self.assertEqual("http://weather.livedoor.com/area/3", self.get_text_kan.get_url())
		self.assertEqual(None, self.get_text_err.get_url())

	def test_get_err_text(self):
		self.assertEqual("以下の地域から選んでください\n"
										 "北海道\n"
										 "東北\n"
										 "関東\n"
										 "信越・北陸\n"
										 "東海\n"
										 "近畿\n"
										 "中国\n"
										 "四国\n"
										 "九州\n"
										 "沖縄\n"
										 , self.get_text_err.get_text())


if __name__ == "__main__":
	unittest.main()
