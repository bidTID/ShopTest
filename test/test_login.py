import allure
from Page.home_page import HomePage
import config


# @allure.severity(allure.severity_level.CRITICAL)
# @allure.feature("用户注册登录")
# @allure.story("用户注册登录流程")
# def test_register_and_login_flow(driver):
#     username = config.USER_PREFIX
#     password = config.PASSWORD
#     email = config.EMAIL
#     address = config.ADDRESS
#     phone = config.MOBILE
#
#     home_page = HomePage(driver)
#
#     with allure.step(f"{username}用户注册,并点击注册按钮"):
#         register_page = home_page.click_register_btn()
#
#     with allure.step(f"输入用户名、密码、确认密码、邮箱、地址、手机号"):
#         login_page = register_page.register(username, password, password, email, address, phone)
#
#     with allure.step(f"用户登录"):
#         home_page = login_page.login(username, password)
#
#     with allure.step(f"获取登录后首页的顶部框件文本"):
#         home_page_after_login_text = home_page.verify_login_page()
#
#     with allure.step(f"断言登录是否成功"):
#         assert username in home_page_after_login_text, \
#             f"登录失败，预期包含 '{username}'，实际文本为 '{home_page_after_login_text}'"


