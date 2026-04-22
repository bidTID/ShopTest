from selenium.webdriver.common.by import By
from Page.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    login_btn = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/a[1]/img')
    register_btn = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/a[2]/img')
    search_input = (By.XPATH, '//*[@id="product_findByName_name"]')
    search_btn = (By.XPATH, '//*[@id="product_findByName_0"]')
    verify_div = (By.ID, 'dark')

    def click_login_btn(self):
        self.find_element(self.login_btn).click()
        from Page.login_page import LoginPage
        return LoginPage(self.driver)

    def click_register_btn(self):
        self.find_element(self.register_btn).click()
        from Page.register_page import RegisterPage
        return RegisterPage(self.driver)

    def search_product(self, keyword):
        self.input_text(self.search_input, keyword)
        self.click(self.search_btn)
        from Page.search_page import SearchPage
        return SearchPage(self.driver)

    def verify_login_page(self):
        # 等待元素可见
        element = self.wait.until(EC.visibility_of_element_located(self.verify_div))
        # 等待元素的文本不为空
        self.wait.until(lambda d: element.text.strip() != "")
        return element.text.strip()