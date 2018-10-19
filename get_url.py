class GetUrl():
	def __init__(self):
		self.area = {"北海道": 1,
								 "東北": 2,
								 "関東": 3,
								 "信越・北陸": 4,
								 "東海": 5,
								 "近畿": 6,
								 "中国": 7,
								 "四国": 8,
								 "九州": 9,
								 "沖縄": 10}

	def get_area_num(self, area_name):
		try:
			area_num = self.area[area_name]
		except KeyError:
			area_num = -1
		return area_num

	def get_url(self, area_name):
		area_num = self.get_area_num(area_name)
		if area_num == -1:
			url = None
		else:
			url = "http://weather.livedoor.com/area/" + str(area_num)
		return url
