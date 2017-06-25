class acctCheck:
	def AccountCheck(self, response):
		try:
			return True if (BeautifulSoup(response.text, "html.parser").find('input', {'name': 'username'})['value'] != "") else False
		except:
			return False
