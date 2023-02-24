import os

import pytest

if __name__ == '__main__':
    pytest.main()
    os.system('-vs allure generate ./temp -o ./report --clean')

    #执行其他文件中的case，用./目标目录
    #执行文件中的类中的某个方法，需要用nodeid指定，格式  ./文件名/类名/方法名