import json
import vidstream_cdn
from mp4upload import mp4 as mp4upload
from vidstream import vpage as vidstream
from xtream import mp4 as xtream
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive 
import requests
folder_id="109wedPCz6jfAv88eRY4OaFrMRRi6eGxp"
movie_json=open("movie_list.json","r")
def upload(aftervideos):
	try:
		f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder_id}],"title":f"{aftervideos}.mp4"})
	except:
		authorize()
		f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder_id}],"title":f"{aftervideos}.mp4"})	
	f.SetContentFile(f"{aftervideos}.mp4")
	f.Upload()
	logger(f'COMPLETED UPLOAD {aftervideos}')
def logger(log):
	file=open("log.txt","a")
	file.write(f'Log --- {log} \n')
	file.close()
def authorize():
	global drive
	try:
		gauth.Authorize()
		drive=GoogleDrive(gauth)
	except:
		try:
			gauth.Refresh()
			drive=GoogleDrive(gauth)
		except Exception as e:
			logger(e)
			print("Errror Occured in" ,e)
def download(link,filename):
	print(link)
	r=requests.get(link,stream=True,verify=False,allow_redirects=True)
	file=open(filename,'wb')
	for ch in r.iter_content(chunk_size=1024*1024):
		if ch:
			file.write(ch)
	file.close()
gauth=GoogleAuth()
gauth.LoadCredentialsFile("animesaga.json")
# Start of the script
movie_list=json.load(movie_json)
for item in movie_list:
	aftervideos=item["anime"]
	filename=f'{aftervideos}.mp4'
	source=vidstream(aftervideos).sources
	id=vidstream(aftervideos).id
	print(source,id)
	try:
		logger(f"Trying Vidstream on {aftervideos}")
		url=vidstream_cdn.mp4(id).file()['url']
		download(url,filename)
		logger(f'COMPLETED DOWNLOAD  with Vidstream---- {aftervideos}')
		upload(aftervideos)
	except:
		try:
			logger("Trying Mp4upload on {aftervideos}")
			file_url=mp4upload(source["Mp4upload"]).file()["url"]
			download(file_url,filename)
			logger(f'COMPLETED DOWNLOAD  with Mp4upload---- {aftervideos}')
			upload(aftervideos)
		except:
			try:
				file_url=xtream(source["Xstreamcdn"]).file()["url"]
				download(file_url,filename)
				logger(f'COMPLETED DOWNLOAD with Xstreamcdn--- {aftervideos}')
				upload(aftervideos)
			except Exception as e:
				print(e)
				logger(f"Download Error Occured in {aftervideos}--- {e}")
