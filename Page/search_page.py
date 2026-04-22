from Page.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    goods_list_div = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/ul[1]/li/table/tbody')
    buy_btn = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/ul[1]/li/table/tbody/tr[5]/td/a/img')

    def buy_goods(self):
        self.click(self.buy_btn)
        from Page.goods_detail_page import GoodsDetailPage
        return GoodsDetailPage(self.driver)

    def get_goods_list(self):
        # 等待元素可见
        element = self.wait.until(EC.visibility_of_element_located(self.goods_list_div))
        # 等待元素的文本不为空
        self.wait.until(lambda d: element.text.strip() != "")
        return element.text.strip()

