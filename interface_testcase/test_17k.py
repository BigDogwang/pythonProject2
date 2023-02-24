import requests
from utils.log_utils import log

req = requests.session()

class Test17k:

    def test_login(self,my_fixture_01):
        url = 'https://passport.17k.com/ck/user/login'
        data = {
            "loginName": "17600087789",
            "password": "cuihao666"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }
        res = req.get(url=url, data=data, headers=headers)
        print(res.json())
        log.info('登陆失败')
        print(my_fixture_01)







