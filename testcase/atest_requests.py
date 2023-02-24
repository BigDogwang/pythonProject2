import re

import pytest
import requests
import json

class TestReq:

    #设置全局变量，通过类名调用
    cooke = ''

    def test_a(self):
        url = 'http://www.xiaohua8.com/xiaohua_238999/'
        res = requests.get(url)
        #print(res.text)
        TestReq.cooke = 'sb'



    #取第一个方法返回值中的一段内容
    def test_b(self):
        url = 'https://api.paugram.com/wallpaper/'
        res = requests.request(method='get',url=url)
        print(res.text)


    def test_c(self):
        url = 'https://tenapi.cn/wdwz/'
        data = {
            "url":"https://www.baidu.com/baidu?tn=34046034_oem_dg&ie=utf-8&wd=%E6%88%91%E6%98%AF%E5%A4%A7%E5%82%BB%E9%80%BC"
        }
        res = requests.request(method='get',url=url,params=data)
        print(res.json())


    def test_d(self):
        url = 'https://tenapi.cn/qr/'
        info = {
            "txt":"im sb",
            "size": "5",
            "margin": "1",
            "ec": "L"
        }
        res = requests.get(url=url,params=info)
        print(res.content)


if __name__ == '__main__':
    TestReq().test_a()
    TestReq().test_c()
    TestReq().test_d()
