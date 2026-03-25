import mysql.connector
from backend.config import Config

# 数据库连接池
connection_pool = None

def get_db_connection():
    """获取数据库连接"""
    global connection_pool
    if connection_pool is None:
        connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="wechat_analysis_pool",
            pool_size=5,
            **Config.DB_CONFIG
        )
    return connection_pool.get_connection()

def init_db():
    """初始化数据库"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 创建会话表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id VARCHAR(36) PRIMARY KEY,
            user_id VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_activity TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        ''')
        
        # 创建分析结果表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            session_id VARCHAR(36) NOT NULL,
            analysis_data TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (session_id) REFERENCES sessions(id)
        )
        ''')
        
        conn.commit()
        print("数据库初始化成功")
    except Exception as e:
        print(f"数据库初始化失败: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()