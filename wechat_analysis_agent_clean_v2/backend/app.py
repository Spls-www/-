from flask import Flask
from backend.api import bp as api_bp
from backend.database import init_db

# 创建 Flask 应用实例
app = Flask(__name__)

# 注册 API 蓝图
app.register_blueprint(api_bp, url_prefix='/api')

# 初始化数据库
init_db()

if __name__ == '__main__':
    # 启动应用
    app.run(debug=True, host='0.0.0.0', port=5000)