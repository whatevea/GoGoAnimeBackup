import requests
from bs4 import BeautifulSoup as bs
class mp4(object):
	"""docstring for mp4"""
	def __init__(self, url):
		self.url=url
		self.api_url=self.url.replace("/v/","/api/source/")
	def file(self):
		self.json_data=requests.post(self.api_url).json()['data']
		response={'url':self.json_data[0]['file']}
		return response


# s2=mp4("https://fcdn.stream/v/x4lg8c51q5731kx")
# print(s2.file())		
# open("try.mp4",'wb').write(requests.get(s2.file()['url']).content)
		