from selene.support.shared import browser
from selene.support.shared.jquery_style import s

"""
Переопределите параметр с помощью indirect
"""
import pytest

url = "https://github.com"


@pytest.fixture(params=[(1200, 900), (500, 300)])
def resolution(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.open(url)


@pytest.mark.parametrize('resolution', [(1200, 900)], indirect=True)
def test_github_desktop(resolution):
    s("[href='/login']").click()



mobile_resolution = pytest.mark.parametrize('resolution', [(500, 300)], indirect=True)

@mobile_resolution
def test_github_mobile(resolution):
    s('.octicon-three-bars').click()
    s("[href='/login']").click()
