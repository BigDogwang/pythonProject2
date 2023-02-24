from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

class TestLojin:

    def test_01(self):
        dri = webdriver.Chrome()
        dri.get('https://www.baidu.com')
        dri.maximize_window()
        # dri.find_element(By.ID,"kw").send_keys("搜索一些内容")
        print(dri.title)
        dri.get_screenshot_as_file()
        # data = dri.get_screenshot_as_png()
        # with open('../ui_photo/搜索截图.jpg','wb') as f:
        #     f.write(data)
        # dri.implicitly_wait(100)#隐式等待，等所有元素都加载出来后在继续
        fat = dri.find_elements()
        print(fat)


        input()







if __name__ == '__main__':
    pytest.main()

