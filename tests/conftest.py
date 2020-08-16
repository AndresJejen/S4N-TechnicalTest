import unittest


from S4NGithubApi.app import create_app
from S4NGithubApi.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)