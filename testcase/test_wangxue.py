from utils.log_utils import *


class TestWang:

    def test_wang_1(self):
        print('王雪1')
        log.info("错误信息，nameerror")
        logging.error('error')
        log.debug('debug')



    def test_wang_2(self,my_fixture):
        print('王雪2')
        print(my_fixture)

if __name__ == '__main__':
    TestWang().test_wang_1()