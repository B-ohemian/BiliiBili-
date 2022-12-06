import requests
import json
import urllib
import os

x = 0  # 图片命名
ID = input("输入UP主ID号:")
PAGE = int(input("请输入下载页数:")) + 1
# PATH = input("请输入要保存的路径，例如“d:\\python\\image:""")


def mkdir(path):  # 创建文件夹
    path = path.strip()  # 去除首位空格
    path = path.rstrip("\\")  # 去除尾部\符号
    isExists = os.path.exists(path)  # 判断路径是否存在

    if not isExists:
        os.mkdir(path)
        print(path + '创建成功')
        return True
    else:
        print(path + '路径已存在')
        return False


def get_images(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'}
    res = requests.get(url, headers=headers)  # 请求
    for video in res.json()['data']['list']['vlist']:
        global x
        urllib.request.urlretrieve(video['pic'], aa + '%s.jpg' % x)  # 用于下载指定url的内容到本地，
        print("正在下载图片，请稍后... No.{}".format(x))
        x += 1


aa = 'C:\\Users\\BOHEMIAN\\Desktop\\image\\'

#C:/Users/BOHEMIAN/Desktop/image
mkdir(aa)

for page in range(1, PAGE):
    url = 'https://api.bilibili.com/x/space/arc/search?mid={}&pn={}&ps=25&index=1&order=pubdate&order_avoided=true&jsonp=jsonp'.format(
        ID,
        page)  # 下载几页
    get_images(url)
# 463999
