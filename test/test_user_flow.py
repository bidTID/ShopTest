import allure
from Page.home_page import HomePage
import config


@allure.feature("用户登录搜索下单购买确认")
def test_user_flow(driver):
    home_page = HomePage(driver)

    # 用户登录并验证
    login_page = home_page.click_login_btn()
    home_page = login_page.login(config.USER_PREFIX, config.PASSWORD)

    with allure.step(f"判断用户登录是否正确"):
        assert config.USER_PREFIX in home_page.verify_login_page(), "登录失败"

    # 搜索商品并验证
    with allure.step(f"在首页搜索框输入关键词'{config.SEARCH_KEYWORD}'并提交"):
        search_page = home_page.search_product(config.SEARCH_KEYWORD)

    with allure.step("获取搜索结果列表的文本内容"):
        goods_list_text = search_page.get_goods_list().lower()
        allure.attach(goods_list_text, name="商品列表文本", attachment_type=allure.attachment_type.TEXT)

    with allure.step(f"验证商品列表包含关键词 '{config.SEARCH_KEYWORD}'"):
        assert config.SEARCH_KEYWORD.lower() in goods_list_text

    # 购买商品
    with allure.step(f"点击购买按钮"):
        goods_details_page = search_page.buy_goods()

    with allure.step(f"点击确认购买按钮"):
        buy_cart_page = goods_details_page.buy_goods()

    # 购物车验证
    with allure.step(f"验证购物车中商品是否符合购买"):
        assert config.SEARCH_KEYWORD.lower() in buy_cart_page.check_goods_detail().lower(), "购物车中商品不符合购买"

    # 确认购买
    order_page = buy_cart_page.click_check_out_btn()

    order_confirm_page = order_page.click_payment_btn()

    my_order_page = order_confirm_page.click_payment_confirm_btn()

    with allure.step(f"验证订单是否成功"):
        assert "已发货" in my_order_page.get_my_order_detail().lower(), "订单未成功"



