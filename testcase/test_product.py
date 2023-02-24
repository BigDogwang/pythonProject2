import time
import pytest

class TestProduct:

    #在每个class类之前只执行一次
    def setup_class(self):
        print('\n在每个class类之前只执行一次')

    #在每个用例执行之前都执行一次
    def setup(self):
        print('\n前置处理，在每个用例执行执前都要执行setup下的内容')

    @pytest.mark.P0
    @pytest.mark.run(order=2)
    def test_01(self):
        print('\n第一')


    @pytest.mark.run(order=1)
    def test_02(self):
        print('\n第二')

    @pytest.mark.skip(reason='无条件跳过')
    def test_03(self):
        print('\n无条件跳过')

    sum = 1
    @pytest.mark.skipif(sum >=1,reason='有条件跳过')
    def test_04 (self):
        print('\n有条件跳过')


    def teardown(self):
        print('\n在每个用例的结尾的时候执行的')


    #在每个class类之后只执行一次
    def teardown_class(self):
        print('\n在每个class类之后只执行一次')


