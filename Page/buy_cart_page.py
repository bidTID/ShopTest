from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BuyCartPage(BasePage):
    goods_detail_div = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/table/tbody/tr[3]')
    check_out_btn = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/table/tbody/tr[4]/td/a[3]/img')

    def click_check_out_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.check_out_btn))
        self.find_element(self.check_out_btn).click()
        from Page.order_page import OrderPage
        return OrderPage(self.driver)

    def check_goods_detail(self):
        # 等待元素可见
        element = self.wait.until(EC.visibility_of_element_located(self.goods_detail_div))
        # 等待元素的文本不为空
        self.wait.until(lambda d: element.text.strip() != "")
        return element.text.strip()