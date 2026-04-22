from selenium.webdriver.common.by import By
from Page.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    username_input = (By.XPATH, '/html/body/div[2]/div[1]/div/form/table/tbody/tr[1]/td[2]/input')
    password_input = (By.XPATH, '/html/body/div[2]/div[1]/div/form/table/tbody/tr[2]/td[2]/input')
    login_button = (By.XPATH, '//*[@id="customer_logon_0"]')

    def login(self, username, password):
        # 检查用户名输入框是否为空，如果为空则输入用户名
        if self.get_value(self.username_input) == '':
            self.find_element(self.username_input).send_keys(username)
        # 检查密码输入框是否为空，如果为空则输入密码
        if self.get_value(self.password_input) == '':
            self.find_element(self.password_input).send_keys(password)
        # 点击登录按钮
        self.find_element(self.login_button).click()
        from Page.home_page import HomePage
        self.wait_for_home_page()
        # 登录成功后返回首页对象
        return HomePage(self.driver)

    # Page/login_page.py

    def wait_for_home_page(self):
        """等待首页标志性元素出现，确保登录成功跳转"""
        # 示例1：等待首页显示的用户名元素（比如你的 verify_div）
        from Page.home_page import HomePage
        home_page = HomePage(self.driver)
        self.wait.until(EC.visibility_of_element_located(home_page.verify_div))