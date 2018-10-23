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
										 "沖縄\n",
										 self.get_text_err.get_text())

	# def test_get_info(self):
		# self.assertEqual("伊豆諸島南部では22日夜遅くまで、小笠原諸島では23日明け方まで、高波に注意してください。"
		# 								 "小笠原諸島では、23日夕方まで急な強い雨や落雷に注意してください。"
		# 								 " 本州付近は、オホーツク海に中心を持つ高気圧に覆われています。"
		# 								 "【関東甲信地方】 関東甲信地方は、おおむね晴れています。"
		# 								 " 22日は、高気圧に覆われて晴れますが、上空の気圧の谷や湿った空気の影響で、次第に曇りとなるでしょう。"
		# 								 " 23日は、気圧の谷や湿った空気の影響により、おおむね曇りですが、昼過ぎにかけては時々晴れる見込みです。"
		# 								 "夜は雨の降る所があるでしょう。"
		# 								 "伊豆諸島南部では、夜遅くには雷雨となる所がある見込みです。"
		# 								 " 関東近海では、22日から23日にかけて、うねりを伴って波が高いでしょう。"
		# 								 "船舶は高波に注意してください。"
		# 								 "【東京地方】 22日は、晴れで夜遅くは曇りとなるでしょう。"
		# 								 " 23日は、曇りで時々晴れる見込みです。",
		# 								 self.get_text_kan.get_info("http://weather.livedoor.com/area/3"))


if __name__ == "__main__":
	unittest.main()
