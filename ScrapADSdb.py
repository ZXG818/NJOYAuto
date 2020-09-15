# coding=utf-8
# 此为从IAEA官网进行下载ACE格式数据库的自动化网络爬虫。
import urllib.request
import re
import os
import time

url = 'https://www-nds.iaea.org/ads/adsace.html'

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'

req = urllib.request.Request(url, headers=head)

response = urllib.request.urlopen(req)

# Data为字符串
data = response.read().decode('utf-8')


# 找到核素名称库
pattern = re.compile('ACE/(.*?).ZIP', re.DOTALL)
nuclear = pattern.findall(data)
print(nuclear)
print(len(nuclear))

download_links = ['https://www-nds.iaea.org/ads/ACE/' + each + '.ZIP' for each in nuclear]


for url in download_links:
    
    print(url)
    
    req = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(req)
    
    data = response.read()    
    
    with open(nuclear[download_links.index(url)]+'.ZIP', 'wb') as f:
        f.write(data)
    
    # 睡眠1s
    time.sleep(1)
print('DONE')
