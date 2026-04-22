from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    @staticmethod
    def create_driver(headless=False):
        options = Options()
        options.add_argument('--no-sandbox')  # 设置浏览器窗口最大化
        options.add_argument('--disable-gpu')  # 禁用GPU加速
        options.add_experimental_option('detach', True)  # 设置浏览器在脚本执行结束后保持打开状态
        options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 排除自动化扩展展示，避免被网站检测为自动化工具
        if headless:  # 设置无头模式
            options.add_argument('--headless')
        service = Service(ChromeDriverManager().install())  # 指定chromedriver.exe的路径
        return webdriver.Chrome(service=service, options=options)  # 返回一个Chrome浏览器实例