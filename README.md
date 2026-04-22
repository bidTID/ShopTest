# Shop 自动化测试框架
基于 Python + Selenium + Pytest + Allure 构建的 Web 自动化测试项目，采用 Page Object Model (POM) 设计模式，覆盖用户登录、注册、商品搜索、加入购物车、下单等核心业务流程。

## 📋 项目特点
- **页面对象模型**：将页面元素与操作分离，提高代码复用性和可维护性。
- **Allure 报告集成**：生成美观、交互式的测试报告，包含失败自动截图功能。
- **日志记录**：关键步骤自动记录日志，便于问题追踪。
- **失败自动截图**：测试失败时自动捕获浏览器截图并附加到报告中。
- **灵活配置**：支持通过命令行参数控制浏览器是否无头运行。
- 
## 📁 项目结构

- **Page/**：页面对象层
  - `BasePage.py`：页面基类，封装通用操作
  - `home_page.py`：首页
  - `login_page.py`：登录页
  - `register_page.py`：注册页
  - `search_page.py`：搜索结果页
  - `goods_details_page.py`：商品详情页
  - `buy_cart_page.py`：购物车页
  - `order_page.py`：订单页
  - `order_confirm_page.py`：订单确认页
- **test/**：测试用例层
  - `test_login.py`：登录注册流程测试
  - `test_search.py`：商品搜索测试
  - `test_user_flow.py`：完整用户购物流程测试
- **utils/**：工具层
  - `driver_factory.py`：浏览器驱动工厂
  - `logger.py`：日志配置
- `config.py`：全局配置文件（URL、测试账号等）
- `conftest.py`：Pytest 固件与钩子（含失败截图逻辑）
- `requirements.txt`：项目依赖

## ⚙️ 环境要求

- Python 3.7+
- Google Chrome 浏览器
- Allure 命令行工具 (用于生成报告)
  
## 📊 查看测试报告
Allure 报告：运行上述命令后会自动打开浏览器展示详细报告，包含测试步骤、失败截图、趋势图表等信息。

pytest-html 报告：项目已集成 pytest-html 插件，运行 pytest --html=report.html 可生成简易 HTML 报告。

## 🖼️ 失败截图功能
测试过程中若发生失败（包括 setup、call 阶段），框架会自动捕获浏览器截图并附加到 Allure 报告中。截图钩子在 conftest.py 中实现，可根据需要调整。
