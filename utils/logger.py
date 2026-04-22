import logging


def setup_logger(name=__name__, level=logging.DEBUG):  # 封装日志管理器方法
    logger = logging.getLogger(name)  # 获取指定名称的日志记录器
    if not logger.handlers:   # 检测日志是否已有处理器
        handler = logging.StreamHandler()   # 创建处理器
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')  # 创建日志格式化
        handler.setFormatter(formatter)  # 为日志管理器设置格式
        logger.addHandler(handler)   # 将处理器添加到日志管理器中
    logger.setLevel(level)   # 设置日志级别
    return logger  # 返回配置好的日志记录器
