from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OrderConfirmPage(BasePage):
    order_confirm_detail_div = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/table/tbody/tr[2]/td/div/table/tbody/tr')
    payment_confirm_btn = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/table/tbody/tr[6]/td/input')

    def get_order_confirm_detail(self):
        return self.find_element(self.order_confirm_detail_div).text

    def click_payment_confirm_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.payment_confirm_btn))
        self.find_element(self.payment_confirm_btn).click()
        from Page.my_order_page import MyOrderPage
        return MyOrderPage(self.driver)
