from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    payment_btn = (By.XPATH, '/html/body/div[2]/form/div/div[6]/table/tbody/tr/td/input')

    def click_payment_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.payment_btn))
        self.find_element(self.payment_btn).click()
        from Page.order_confirm_page import OrderConfirmPage
        return OrderConfirmPage(self.driver)
