import pytest

class Testapi:

    @pytest.mark.parametrize('name',['王雪','崔浩'])
    def test_api(self,name):
        print(name)


    @pytest.mark.parametrize('name,age',[['王雪',18],['崔浩',20]])
    def test_api2(self,name,age):
        print(name,age)


