import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup as bs
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class mp4(object):
	def __init__(self,url):
		self.url=url.replace("embed-","").replace(".html","")
		html=requests.get(self.url).text
		self.soup=bs(html,'html.parser')
		self.fileName=self.soup.h2.text
		self.fileName=self.fileName.replace('Download File ','')
		self.size=self.soup.find('div',{"id":"container"}).div.font.text
		self.size=re.findall(r'\d+', self.size)[-2]
	def press(self):
		params=dict()
		inputs=self.soup.find_all('input')
		for item in inputs:
			params.update({item['name']:item['value']})
		response=requests.post(self.url,data=params).text
		return response
	def file(self):
		soup=bs(self.press(),'html.parser')
		params=dict()
		inputs=soup.find_all('input')
		for item in inputs:
			params.update({item['name']:item['value']})
		response=requests.post(self.url,data=params,verify=False,allow_redirects=False).headers['Location']
		return {"url":response,"size":self.size,"filename":self.fileName}
# s2=mp4("https://www.mp4upload.com/embed-i7od6arqmpj4.html")
# print("doing")
# print(s2.file())
# print("done")
