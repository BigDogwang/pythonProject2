import pytest
import requests
import allure
from utils.log_utils import Log_utils
from utils.yaml_operation import YamlOperation


class Testtianqi:

    @allure.step("第一步")
    @pytest.mark.parametrize('name',YamlOperation.read_yaml('./data/data_tianqi.yaml','test_tianqi'))#yaml这段是直接拿yamloperation类中主函数执行那块的代码
    def test_tianqi_0(self,name):
        url = 'https://tenapi.cn/wether/'
        info = {
            "city":name["city"]
        }
        res = requests.get(url=url,params=info)
        #print(res.json())
        assert res.status_code == name["code"]


    @allure.step("第二步")
    @pytest.mark.parametrize('name', YamlOperation.read_yaml('./data/data_tianqi.yaml','test_tianqi'))
    def test_tianqi2(self,name):
        url = 'https://tenapi.cn/wether/'
        info = {
            "city": name["city"]
        }
        res = requests.get(url=url, params=info)
        #print(res.json())
        assert res.status_code == name["code"]
