from flask import request, jsonify
from backend.api import bp
from backend.database import get_db_connection
import uuid
from datetime import datetime

@bp.route('/sessions', methods=['POST'])
def create_session():
    """创建新会话"""
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        
        if not user_id:
            return jsonify({"success": False, "error": "缺少 user_id 参数"}), 400
        
        # 生成会话 ID
        session_id = str(uuid.uuid4())
        
        # 保存到数据库
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO sessions (id, user_id) VALUES (%s, %s)",
            (session_id, user_id)
        )
        
        conn.commit()
        
        return jsonify({
            "success": True,
            "session_id": session_id,
            "created_at": datetime.now().isoformat()
        })
    except Exception as e:
        print(f"创建会话失败: {e}")
        return jsonify({"success": False, "error": str(e)}), 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@bp.route('/sessions/<session_id>', methods=['GET'])
def get_session(session_id):
    """获取会话信息"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute(
            "SELECT * FROM sessions WHERE id = %s",
            (session_id,)
        )
        
        session = cursor.fetchone()
        
        if not session:
            return jsonify({"success": False, "error": "会话不存在"}), 404
        
        return jsonify({
            "success": True,
            "session": session
        })
    except Exception as e:
        print(f"获取会话失败: {e}")
        return jsonify({"success": False, "error": str(e)}), 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()