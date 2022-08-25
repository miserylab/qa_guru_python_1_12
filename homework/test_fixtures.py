"""
Сделайте разные фикстуры для каждого теста
"""
import pytest
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

url = "https://github.com"


@pytest.fixture(scope="function")
def browser_desktop():
    browser.config.window_width = 1200
    browser.config.window_height = 900


@pytest.fixture(scope="function")
def browser_mobile():
    browser.config.window_width = 500
    browser.config.window_height = 300


def test_github_desktop(browser_desktop):
    browser.open(url)
    s("[href='/login']").click()


def test_github_mobile(browser_mobile):
    browser.open(url)
    s('.octicon-three-bars').click()
    s("[href='/login']").click()
