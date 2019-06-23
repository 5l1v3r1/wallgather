#!/usr/bin/python
from bs4 import BeautifulSoup
from datetime import date
import requests,urllib,time
def get_wp(url):
	urllib.urlretrieve(url,str(int(round(time.time() * 1000)))+"_"+str(date.today())+".jpg")
def download(halaman):
	print "[*] Current Page :",halaman
	r=requests.get("https://wallpaperscraft.com/catalog/anime/page"+str(halaman))
	soup=BeautifulSoup(r.text,"html.parser").find_all('img',attrs={'class':'wallpapers__image'})
	for i in range(len(soup)):
		if get_wp(soup[i].get('src').replace('300x168','1280x720')):
			print ""
		else:
			print "["+str(i)+"]","-> SUCCESS"
	download(int(halaman)+1)
print "[ WallGather | WibuTools ] -> Copyright by FilthyRoot\n"
xx=raw_input("Halaman : ")
if xx:
	download(xx)
else:
	print "Masukan halaman!"
