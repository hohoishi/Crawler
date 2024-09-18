from urllib.request import urlopen , Request
from bs4 import BeautifulSoup 
import requests
from ptt_beauty import post_download


url = 'https://www.ptt.cc/bbs/Beauty/index4003.html'
header = {'User-Agent':'',
         'Cookie' :'over18=1' }
response = requests.get(url , headers=header)
html = BeautifulSoup(response.text)
title = html.find_all('div', {'class':'title'})
    
for t in title:
    if t.find('a'):
        href = 'https://www.ptt.cc/' + t.find('a')['href']
        print(href)
        post_download(href)