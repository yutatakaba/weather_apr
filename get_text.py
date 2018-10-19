from get_url import GetUrl


class GetText():
	def __init__(self, area):
		self.got_url = GetUrl()
		self.url = self.got_url.get_url(area)

	def get_url(self):
		url = self.url
		return url

	def get_text(self):
		err_text = '以下の地域から選んでください\n北海道\n東北\n関東\n信越・北陸\n東海\n近畿\n中国\n四国\n九州\n沖縄\n'
		url = self.get_url()
		if url is None:
			return err_text
		# else:
		# 	text =
