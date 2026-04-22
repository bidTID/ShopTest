from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger


class BasePage:

    def __init__(self, driver):

        self.driver = driver  # 封装驱动管理器
        self.wait = WebDriverWait(self.driver, 10)  # 设置显示等待时间
        self.logger = setup_logger(self.__class__.__name__)  # 初始化日志管理器

    # 指定打开URL的方法
    def open_url(self, url):

        self.logger.info(f"打开网页: {url}") # 记录打开页面的日志
        self.driver.get(url)  # 打开页面

    # 封装查找元素的方法
    def find_element(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)  # 设置显示等待时间
            element = wait.until(EC.presence_of_element_located(locator)) # 等待元素出现
            self.logger.debug(f"找到元素: {locator}") # 记录找到元素的日志
            return element  # 返回找到的元素
        except Exception as e:
            self.logger.error(f"找不到元素: {locator}") # 记录找不到元素的日志
            raise e  # 抛出异常

    # 封装点击元素的方法
    def click(self,locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator)) # 等待元素可点击
            element.click()  # 点击元素
            self.logger.debug(f"点击元素: {locator}")  # 记录点击元素的日志
        except Exception as e:
            self.logger.error(f"找不到元素: {locator}")  # 记录找不到元素的日志
            raise e  # 抛出异常

    # 封装输入文本的方法
    def input_text(self, locator, text, clear_first=True, timeout=10):
        try:
            element = self.find_element(locator)  # 查找元素
            if clear_first:
                element.clear()  # 清空输入框
            element.send_keys(text)  # 输入文本
            self.logger.debug(f"输入文本: {text}")  # 记录输入文本的日志
        except Exception as e:
            self.logger.error(f"找不到元素: {locator}") # 记录找不到元素的日志
            raise e  # 抛出异常

    # 封装获取元素文本的方法
    def get_text(self, locator, timeout=10):
        try:
            element = self.find_element(locator)  # 查找元素
            text = element.text  # 获取元素文本
            self.logger.debug(f"获取元素文本: {text}")  # 记录获取元素文本的日志
            return text  # 返回元素文本
        except Exception as e:
            self.logger.error(f"找不到元素: {locator}")  # 记录找不到元素的日志
            raise e  # 抛出异常

    def get_value(self, locator, timeout=10):
        """获取输入框或文本域的 value 属性值"""
        try:
            element = self.find_element(locator)
            value = element.get_attribute('value')
            self.logger.debug(f"获取元素值: {value}")
            return value
        except Exception as e:
            self.logger.error(f"获取元素值失败: {locator}")
            raise e