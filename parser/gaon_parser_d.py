# -*- coding: utf-8 -*-

# 작성자 : 강성훈 (devholic@plusquare.com)

import sqlite3
import urllib2
from bs4 import BeautifulSoup

conn = sqlite3.connect('db.sqlite3')

chart = u"가온 디지털 차트"
for i in range(2015, 2016):
	year = str(i)
	for j in range(26,27):
		if j <= 9:
			week = "0" + str(j)
		else:
			week = str(j)
		print year + ":" + week
		url = "http://gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&targetTime="+week+"&hitYear="+year+"&termGbn=week"
		data = urllib2.urlopen(url)
		soup = BeautifulSoup(data)
		rank = soup.find("td", { "class" : "subject" })
		r = rank.findAll("p")
		song = r[0].contents[0].string #노래
		singer = r[1].contents[0].string #가수
		album = r[1].contents[2].string #앨범
		song = unicode(song)
		singer = unicode(singer)
		album = unicode(album)
		print song
		c = conn.cursor()
		c.execute('''INSERT INTO timeline_web_rankdata (chart,year,week,title,artist,album, youtube) VALUES (?,?,?,?,?,?,?)''', (chart,int(year),int(week),song,singer,album,"http://"))
		conn.commit()

conn.close()
