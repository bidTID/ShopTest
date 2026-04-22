from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GoodsDetailPage(BasePage):
    instant_buy_btn = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/ul[1]/li/table/tbody/tr[5]/td/a/img')
    goods_detail_div = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/ul[1]')
    goods_introduce_div = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/ul[3]/li/p')

    def buy_goods(self):
        self.wait.until(EC.visibility_of_element_located(self.instant_buy_btn))
        self.click(self.instant_buy_btn)
        from Page.buy_cart_page import BuyCartPage
        return BuyCartPage(self.driver)

    def get_goods_detail(self):
        return self.find_element(self.goods_detail_div).text

    def get_goods_introduce(self):
        return self.find_element(self.goods_introduce_div).text