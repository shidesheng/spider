#!/usr/bin/env python3  
#coding: utf-8
# -*- coding: utf-8 -*-
import urllib3,urllib,time,re,sys,ssl,os
from urllib import request
import urllib.request
import subprocess



ssl._create_default_https_context = ssl._create_unverified_context
url = "https://mirrors.cnnic.cn/adobe-fonts/"
page = request.urlopen(url)
html = page.read().decode('utf-8') 

#使用正则对源码html中匹配.jar的绝对url地址
reg = r'<a href="(.+?[o,f,s]\/)">' 
dwre = re.compile(reg) 
dwlist = re.findall(dwre,html) 
print (dwlist)
localpath = r'./OTF'
for ul in dwlist:
	ssl._create_default_https_context = ssl._create_unverified_context
	print ("https://mirrors.cnnic.cn/adobe-fonts/"+ul+"OTF/")
	urlxx = 'https://mirrors.cnnic.cn/adobe-fonts/'+ul+'OTF/'
   # print (urlxx)
	pagexx = request.urlopen(urlxx)
	htmlxx = pagexx.read().decode('utf-8') 

#使用正则对源码html中匹配.jar的绝对url地址
	regxx = r'<a href="(.+?\.otf)">' 
	dwrexx = re.compile(regxx) 
	dwlistxx = re.findall(dwrexx,htmlxx) 
	print (dwlistxx)
	for filename in dwlistxx:
		url_filename = os.path.basename(filename)
		dest_dir = os.path.join(localpath,url_filename)
		url2=urlxx+filename
		urllib.request.urlretrieve(url2,dest_dir)
		print(dest_dir)
#方法2

