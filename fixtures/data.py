import pytest


@pytest.fixture(scope="session")
def base_document():
    return 'CV - TEST'
