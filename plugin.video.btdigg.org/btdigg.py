#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib
#import re
#import sys
import os
import Cookie

import string, xbmc, xbmcgui, xbmcplugin, urllib, cookielib, xbmcaddon
#-------------------------------
import urllib, urllib2, time, random
#from time import gmtime, strftime 
#from urlparse import urlparse 

import HTMLParser 
hpar = HTMLParser.HTMLParser()
#-----------------------------------------
import socket
socket.setdefaulttimeout(50)

icon = ""
siteUrl = 'api.btdigg.org/api/private-c47ba652ee73735a/s02'
httpSiteUrl = 'http://' + siteUrl
sid_file = os.path.join(xbmc.translatePath('special://temp/'), 'btdigg.cookies.sid')#'plugin.video.krasfs.ru.cookies.sid'

#h = int(sys.argv[1])


#--------------- 
cj = cookielib.FileCookieJar(sid_file) 
hr  = urllib2.HTTPCookieProcessor(cj) 
opener = urllib2.build_opener(hr) 
urllib2.install_opener(opener) 

def unescape(text): 
    try: 
        text = hpar.unescape(text) 
    except: 
        text = hpar.unescape(text.decode('utf8')) 

    try: 
        text = unicode(text, 'utf-8') 
    except: 
        text = text 

    return text 
#--------------- 
url='http://www.btdigg.org/' 

#-- step 1 - get session cookies 
post = None 
request = urllib2.Request(url, post) 

request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)') 
request.add_header('Host',    'www.krasfs.ru') 
request.add_header('Accept', '*/*') 
request.add_header('Accept-Language', 'ru-RU') 
request.add_header('Referer',    'http://www.btdigg.org') 

try: 
    f = urllib2.urlopen(request) 
except IOError, e: 
    if hasattr(e, 'reason'): 
        xbmc.log('We failed to reach a server. Reason: '+ e.reason) 
    elif hasattr(e, 'code'): 
        xbmc.log('The server couldn\'t fulfill the request. Error code: '+ e.code)

# ---------------------------------------

def showMessage(heading, message, times = 3000):
	xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")'%(heading, message, times, icon))

def ru(x):return unicode(x,'utf8', 'ignore')
def xt(x):return xbmc.translatePath(x)

def formtext(http):
	#http=http.replace(chr(10),"")#.replace(chr(13),"")
	http=http.replace("'",'"').replace('&nbsp;'," ")#���������
	http=http.replace('           <',"<").replace('          <',"<").replace('         <',"<").replace('        <',"<").replace('       <',"<").replace('      <',"<").replace('     <',"<").replace('    <',"<").replace('   <',"").replace('  <',"<").replace(' <',"<")
	http=http.replace('&amp;nbsp;',"")
	#http=http.replace('</a> </td> <td align=center>',"', '").replace('</td> </tr>  <tr> <td align=left>  ',"']"+chr(10)).replace('> ',"', '")
	#http=cleartext(http)
	
	return http

def formating(str):
	str=str.strip()
	str=str.replace('%','%25')
	str=str.replace('&','%26')
	str=str.replace('?','%3F')
	str=str.replace('&','%26')
	str=str.replace('!','%21')
	str=str.replace(':','%3A')
	str=str.replace('#','%23')
	str=str.replace(',','%2C')
	str=str.replace(';','%3B')
	str=str.replace('@','%40')
	str=str.replace('(','%28')
	str=str.replace(')','%29')
	str=str.replace('"','%22')
	
	str=str.replace('�','%E0')
	str=str.replace('�','%E1')
	str=str.replace('�','%E2')
	str=str.replace('�','%E3')
	str=str.replace('�','%E4')
	str=str.replace('�','%E5')
	str=str.replace('�','%b8')
	str=str.replace('�','%E6')
	str=str.replace('�','%E7')
	str=str.replace('�','%E8')
	str=str.replace('�','%E9')
	str=str.replace('�','%EA')
	str=str.replace('�','%EB')
	str=str.replace('�','%EC')
	str=str.replace('�','%ED')
	str=str.replace('�','%EE')
	str=str.replace('�','%EF')
	str=str.replace('�','%F0')
	str=str.replace('�','%F1')
	str=str.replace('�','%F2')
	str=str.replace('�','%F3')
	str=str.replace('�','%F4')
	str=str.replace('�','%F5')
	str=str.replace('�','%F6')
	str=str.replace('�','%F7')
	str=str.replace('�','%F8')
	str=str.replace('�','%F9')
	str=str.replace('�','%FA')
	str=str.replace('�','%FB')
	str=str.replace('�','%FC')
	str=str.replace('�','%FD')
	str=str.replace('�','%FE')
	str=str.replace('�','%FF')
	
	str=str.replace('�','%C0')
	str=str.replace('�','%C1')
	str=str.replace('�','%C2')
	str=str.replace('�','%C3')
	str=str.replace('�','%C4')
	str=str.replace('�','%C5')
	str=str.replace('�','%A8')
	str=str.replace('�','%C6')
	str=str.replace('�','%C7')
	str=str.replace('�','%C8')
	str=str.replace('�','%C9')
	str=str.replace('�','%CA')
	str=str.replace('�','%CB')
	str=str.replace('�','%CC')
	str=str.replace('�','%CD')
	str=str.replace('�','%CE')
	str=str.replace('�','%CF')
	str=str.replace('�','%D0')
	str=str.replace('�','%D1')
	str=str.replace('�','%D2')
	str=str.replace('�','%D3')
	str=str.replace('�','%D4')
	str=str.replace('�','%D5')
	str=str.replace('�','%D6')
	str=str.replace('�','%D7')
	str=str.replace('�','%D8')
	str=str.replace('�','%D9')
	str=str.replace('�','%DA')
	str=str.replace('�','%DB')
	str=str.replace('�','%DC')
	str=str.replace('�','%DD')
	str=str.replace('�','%DE')
	str=str.replace('�','%DF')
	str=str.replace(' ','+')
	return str

def inputbox():
	skbd = xbmc.Keyboard()
	skbd.setHeading('�����:')
	skbd.doModal()
	if skbd.isConfirmed():
		SearchStr = skbd.getText()
		return SearchStr
	else:
		return ""


def upd(category, sort, s):
		request = urllib2.Request('http://api.btdigg.org/api/private-c47ba652ee73735a/s02?q='+s.replace(" ","+")+"&order=1")

		request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)') 
		request.add_header('Accept', '*/*') 
		request.add_header('Accept-Language', 'ru-RU') 
		#request.add_header('Referer',    'http://www.btdigg.org') 
		Lout=[]
		try: 
			f = urllib2.urlopen(request) 
			html = f.read()
			list=eval(html)
			for i in list:
				info_hash=i["info_hash"]
				name=str(i["name"])
				files=i["files"]
				reqs=i["reqs"]
				magnet=i["magnet"]
				weight=i["weight"]
				size=i["size"]
				torrent='http://torcache.net/torrent/'+info_hash+".torrent"
				Lout.append([str(weight),str(size),xt(name),torrent])
			return Lout
		except IOError, e: 
			if hasattr(e, 'reason'): 
				print 'We failed to reach a server. Reason: '+ e.reason
			elif hasattr(e, 'code'): 
				print 'The server couldn\'t fulfill the request. Error code: '+ e.code
			return ""


def format(L):
		if L==None: 
			return ["","","","","","","","",""]
		else:
			Ln=[]
			i=0
			tmp1=''
			tmp2=''
			tmp3=''
			for itm in L:
				i+=1
				if len(itm)>6:
					if itm[:5]=="</out":
						i=0
						Ln.append([" -- ",tmp3,tmp2,tmp1])
					elif itm[:4]=="<has":
						tmp1='https://krasfs.ru/download.php?hash='+itm[6:-7]
					elif itm[:4]=="<alt":
						tmp2=itm[10:-11]
					elif itm[:6]=="<sizef":
						tmp3=itm[7:-8]
			return Ln
			
class Tracker:
	def __init__(self):
		pass

	def Search(self, text="matrix", category=4):
		sort='newest'
		L=upd(category, sort, xt(text))
		return L