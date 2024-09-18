"""Module docstring"""
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    """Read input parameters"""
    parser.addoption(
        "--url",
        action="store",
        default="https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a"
    )
    parser.addoption(
        "--selenium_hub",
        action="store",
        required=True
    )


@pytest.fixture(scope="session", autouse=True)
def user_options(pytestconfig):
    """Returns test parameters"""
    return {
        "URL": pytestconfig.getoption("url"),
        "SELENIUM_HUB": pytestconfig.getoption("selenium_hub")
    }


@pytest.fixture
def browser(user_options):
    """Returns the browser instance"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument('disable-notifications')
    b = webdriver.Remote(command_executor=user_options["SELENIUM_HUB"], options=options)
    b.implicitly_wait(10)
    yield b
    b.quit()
