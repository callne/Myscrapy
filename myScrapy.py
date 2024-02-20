import pandas as pd
import os
import selenium.webdriver
import urllib3
import bs4
import requests
import re
import threading
import easygui as g
from urllib.request import urlretrieve
g.msgbox("点击下面按钮选取文件",'5毛钱ui','选取')
fin = g.fileopenbox()
print(fin)



headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)',
    'Host':'httpbin.org'}
http = urllib3.PoolManager()


df = pd.read_excel(io=fin)
df_list = df.values.tolist()
result = []
for i in df_list:
  result.append(i[0])
print(result)
for i in result:
  r = http.request('Get', i)
  page = r.data.decode('utf-8')
  a = bs4.BeautifulSoup(page, 'html.parser')
  q = repr(a.img.attrs['src'])# 网页获取源码
  print(q)
  match = re.search('o=', q)  # 中文名字获取
  b = a.img.attrs['src'][match.start():] + '.jpg'
  c = a.img.attrs['src'][match.start():]
  total = "https://air.scjgj.gz.gov.cn" + "/cancelEasy/commonquery/getBusinessLicenceImg?uniscid=91440101MA5D5T047J"+r'&regno'+c  # 获取图片下载地址

  img_url = requests.get(total,headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
  })  # 保存图片到当前文件夹

  with open(b, 'wb') as f:
    f.write(img_url.content)

