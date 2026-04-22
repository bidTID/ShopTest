from Page.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    username_input = (By.NAME, 'username')
    password_input = (By.NAME, 'password')
    repassword_input = (By.NAME, 'repassword')
    email_input = (By.NAME, 'email')
    address_input = (By.NAME, 'address')
    mobile_input = (By.NAME, 'mobile')
    register_btn = (By.XPATH, '//*[@id="customer_save_0"]')

    def register(self, username, password, repassword, email, address, mobile):

        """
        用户注册功能方法
        :param username: 用户名
        :param password: 密码
        :param repassword: 确认密码
        :param email: 电子邮箱
        :param address: 地址
        :param mobile: 手机号码
        :return: 返回登录页面实例
        """
        self.input_text(self.username_input, username)  # 在用户名输入框输入用户名
        self.input_text(self.password_input, password)  # 在密码输入框输入密码
        self.input_text(self.repassword_input, repassword)  # 在确认密码输入框输入确认密码
        self.input_text(self.email_input, email)  # 在邮箱输入框输入电子邮箱
        self.input_text(self.address_input, address)  # 在地址输入框输入地址
        self.input_text(self.mobile_input, mobile)  # 在手机号输入框输入手机号码
        self.click(self.register_btn)  # 点击注册按钮
        from Page.login_page import LoginPage
        return LoginPage(self.driver)  # 注册完成后返回登录页面实例
