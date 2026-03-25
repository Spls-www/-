import os
from dotenv import load_dotenv

# 加载环境变量（从项目根目录）
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
env_path = os.path.join(project_root, '.env')
load_dotenv(env_path)
print(f"加载环境变量文件: {env_path}")

class Config:
    """配置类"""
    # 数据库配置
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'wechat_analysis')
    
    # API配置
    GPT_API_KEY = os.getenv('GPT_API_KEY', '')
    GPT_API_URL = os.getenv('GPT_API_URL', 'https://api.openai.com/v1/chat/completions')
    COZE_API_KEY = os.getenv('COZE_API_KEY', '')
    VOLC_API_KEY = os.getenv('VOLC_API_KEY', '')
    VOLC_API_URL = os.getenv('VOLC_API_URL', 'https://ark.cn-beijing.volces.com/api/v3/chat/completions')
    VOLC_MODEL_NAME = os.getenv('VOLC_MODEL_NAME', '')
    # 火山方舟配置
    ARK_API_KEY = os.getenv('ARK_API_KEY', '')
    ARK_BASE_URL = os.getenv('ARK_BASE_URL', 'https://ark.cn-beijing.volces.com/api/v3')
    
    # 应用配置
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    
    # 数据库连接配置
    DB_CONFIG = {
        'user': DB_USER,
        'password': DB_PASSWORD,
        'host': DB_HOST,
        'database': DB_NAME,
        'raise_on_warnings': True
    }