import requests
class mp4(object):
	"""docstring for mp4"""
	def __init__(self, id):
		self.url="https://vidstreaming.io/ajax.php?id="+id
		json_data=requests.get(self.url).json()
		self.link="not found"
		if "goto.php" in json_data['source'][0]['file']:
			self.link=json_data['source'][0]['file']
		elif "goto.php" in json_data['source_bk'][0]['file']:
			self.link=json_data['source_bk'][0]['file']
	def file(self):
		return {"url":self.link}
# demo=mp4("MTQzMTM5")
# print("doing",demo.link)
# open("try.mp4",'wb').write(requests.get(demo.link).content)
# print("done")