import allure
from Page.home_page import HomePage
import config


# @allure.severity(allure.severity_level.BLOCKER)
# @allure.feature("商品搜索")
# @allure.story("用户通过关键词搜索商品")
# @allure.title("搜索存在的商品关键词并返回相关结果")
# def test_search(driver):
#     home_page = HomePage(driver)
#
#     with allure.step(f"在首页搜索框输入关键词'{config.SEARCH_KEYWORD}'并提交"):
#         search_page = home_page.search_product(config.SEARCH_KEYWORD)
#
#     with allure.step("获取搜索结果列表的文本内容"):
#         goods_list_text = search_page.get_goods_list().lower()
#         allure.attach(goods_list_text, name="商品列表文本", attachment_type=allure.attachment_type.TEXT)
#
#     with allure.step(f"验证商品列表包含关键词 '{config.SEARCH_KEYWORD}'"):
#         assert config.SEARCH_KEYWORD.lower() in goods_list_text


