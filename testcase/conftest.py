import pytest

@pytest.fixture(scope='function',params=['成龙','甄子丹','戴艺林'],ids=['cl','zzd','cyl'])#,params='',autouse=False,ids='',name=''
def my_fixture(request):
    print('\n前置')
    yield request.param             #return和yield都是返回的意思，return后面不能接代码，yield后面可以接代码
    print('\n后置')