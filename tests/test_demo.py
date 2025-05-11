import pytest
import logging

logging.basicConfig(level=logging.INFO)


@pytest.fixture
def example_fixture():
    logging.info("Setting up example fixture")
    return 1


def test_with_fixture(example_fixture):
    assert example_fixture == 1
