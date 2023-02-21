import json
import os

import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='chrome')


@pytest.fixture(scope='session')
def config():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"config/test_env.json")) as f:
        return json.load(f)
