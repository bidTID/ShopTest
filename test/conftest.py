import logging
import pytest
from utils.driver_factory import DriverFactory
from config import BASE_URL
import allure
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )


@pytest.fixture(scope="function")
def driver(request):
    headless = request.config.getoption("--headless")
    driver_instance = DriverFactory.create_driver(headless)
    try:
        driver_instance.maximize_window()
    except Exception:
        driver_instance.set_window_size(1920, 1080)
    driver_instance.get(BASE_URL)
    yield driver_instance
    driver_instance.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver', None)
        if driver:
            # 必须在此处使用 allure 的步骤上下文
            with allure.step("截图并附加"):
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
