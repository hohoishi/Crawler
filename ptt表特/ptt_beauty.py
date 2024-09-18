
from urllib.request import urlopen , Request
from bs4 import BeautifulSoup 
import requests
import os
import time
def post_download(url):
    # url = 'https://www.ptt.cc/bbs/Beauty/M.1713327887.A.3DA.html'
    header = {'User-Agent':'',
            'Cookie' :'over18=1' }
    dirname = os.path.join('beauty/',url.split('/')[-1] )
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    response = requests.get(url , headers=header)
    html = BeautifulSoup(response.text)
    links = html.find_all('a')
    reserved = ['img' ,'png','jpg','jpeg','gif']
    for l in links :
        href = l['href']
        sub = href.split('.')[-1]
        if sub.lower() in reserved:
            print('下載', href)
            fp = os.path.join(dirname, href.split('/')[-1])
            response = requests.get(href, stream=True, headers=header) #多加header因為變嚴格
            img = response.raw.read()
            f = open(fp, 'wb')
            f.write(img)
            f.close()
            time.sleep(0.5)
        
        print('-'*30)