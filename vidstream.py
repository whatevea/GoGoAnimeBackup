from bs4 import BeautifulSoup as bs
import requests
class vpage(object):
	"""docstring for vpage"""
	def __init__(self, aftervideos):
		url = "https://vidstreaming.io/videos/"+aftervideos
		html=requests.get(url).text
		url="https:"+bs(html,'html.parser').iframe['src']
		html=requests.get(url).text
		soup=bs(html,'html.parser')
		self.id=url.split("?id=")[1].split("&title")[0]
		self.sources={}
		linkservers=soup.find_all('li',{"class":"linkserver"})
		for item in linkservers:
			self.sources.update({item.text:item['data-video']})
# demopage=vpage("peter-grill-to-kenja-no-jikan-uncensored-episode-4")
# print(demopage.sources)
