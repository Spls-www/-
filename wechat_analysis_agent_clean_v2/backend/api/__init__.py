from flask import Blueprint

# 创建 API 蓝图
bp = Blueprint('api', __name__)

# 导入各个 API 模块
from backend.api import recommendations, sessions