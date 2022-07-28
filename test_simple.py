import pytest
import time


@pytest.fixture()
def browser():
    time.sleep(1)


def test_first(browser):
    time.sleep(1)


def test_second():
    time.sleep(1)


def test_third():
    time.sleep(1)
