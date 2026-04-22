import openpyxl
BASE_URL = "http://192.168.91.128:8080/Shop/index.html" #测试地址
DEFAULT_TIMEOUT = 10  # 默认超时时间
xl = openpyxl.load_workbook("../Shop/config.xlsx")
sheet = xl['Sheet1']
USER_PREFIX = "cyanday"
PASSWORD = sheet['B2'].value
EMAIL = sheet['C2'].value
ADDRESS = sheet['D2'].value
MOBILE = sheet['E2'].value
SEARCH_KEYWORD = sheet['F2'].value