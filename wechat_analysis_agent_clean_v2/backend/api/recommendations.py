from flask import request, jsonify
from backend.api import bp
from backend.config import Config
import json
import time
import requests

# 尝试导入火山引擎 SDK
try:
    from volcengine.ark.runtime import Ark
    has_volc_sdk = True
except ImportError:
    has_volc_sdk = False

def call_volc_api(prompt, max_retries=3, timeout=600):
    """调用火山引擎 API 获取推荐"""
    retries = 0
    while retries < max_retries:
        try:
            if has_volc_sdk and Config.ARK_API_KEY:
                # 使用 SDK 调用
                ark = Ark(
                    base_url=Config.ARK_BASE_URL,
                    api_key=Config.ARK_API_KEY
                )
                response = ark.chat.completions.create(
                    model=Config.VOLC_MODEL_NAME or "ep-20260324141731-78xx5",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=1000,
                    temperature=0.7
                )
                return response.choices[0].message.content
            elif Config.ARK_API_KEY:
                # 使用 HTTP 调用
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {Config.ARK_API_KEY}"
                }
                data = {
                    "model": Config.VOLC_MODEL_NAME or "ep-20260324141731-78xx5",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 1000,
                    "temperature": 0.7
                }
                response = requests.post(
                    f"{Config.ARK_BASE_URL}/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=timeout
                )
                response.raise_for_status()
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                return "请配置 ARK_API_KEY"
        except Exception as e:
            print(f"调用火山引擎 API 失败: {e}")
            retries += 1
            if retries < max_retries:
                print(f"重试中... ({retries}/{max_retries})")
                time.sleep(3)
            else:
                return f"API 调用失败: {str(e)}"

@bp.route('/recommendations', methods=['POST'])
def get_recommendations():
    """获取推荐"""
    try:
        data = request.get_json()
        session_id = data.get('session_id')
        analysis_data = data.get('analysis_data')
        
        if not session_id or not analysis_data:
            return jsonify({"success": False, "error": "缺少必要参数"}), 400
        
        # 构建提示词
        prompt = f"基于以下微信公众号分析数据，提供有价值的推荐：\n{json.dumps(analysis_data, ensure_ascii=False)}"
        
        # 调用火山引擎 API
        recommendations = call_volc_api(prompt)
        
        # 解析推荐结果
        recommendation_list = recommendations.split('\n') if isinstance(recommendations, str) else []
        recommendation_list = [r.strip() for r in recommendation_list if r.strip()]
        
        return jsonify({
            "success": True,
            "recommendations": recommendation_list,
            "session_id": session_id
        })
    except Exception as e:
        print(f"处理推荐请求失败: {e}")
        return jsonify({"success": False, "error": str(e)}), 500