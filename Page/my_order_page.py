from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MyOrderPage(BasePage):
    my_order_detail_div = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr')

    def get_my_order_detail(self):
        # 等待元素可见
        element = self.wait.until(EC.visibility_of_element_located(self.my_order_detail_div))
        # 等待元素的文本不为空
        self.wait.until(lambda d: element.text.strip() != "")
        return element.text.strip()
