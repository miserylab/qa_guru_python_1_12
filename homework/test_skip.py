"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

url = "https://github.com"


@pytest.fixture(params=[{'resolution': 'desktop', 'width': 1200, 'height': 900},
                        {'resolution': 'mobile', 'width': 500, 'height': 300}])
def resolution_check(request):
    browser.config.window_width = request.param['width']
    browser.config.window_height = request.param['height']
    browser.open(url)
    return request.param['resolution']


def test_github_desktop(resolution_check):
    if resolution_check == 'mobile':
        pytest.skip('Wrong window size. Reseason: Mobile resolution')
    s("[href='/login']").click()


def test_github_mobile(resolution_check):
    if resolution_check == 'desktop':
        pytest.skip('Wrong window size. Reseason: Desktop resolution')
    s('.octicon-three-bars').click()
    s("[href='/login']").click()
