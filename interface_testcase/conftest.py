import pytest

@pytest.fixture(scope="function",params=['cuihao','wangxue'])
def my_fixture_01(request):
    return request.param
