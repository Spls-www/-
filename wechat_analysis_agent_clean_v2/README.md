# 微信分析助手项目

## 项目简介

微信分析助手是一个基于 Flask 的 web 应用，用于分析微信公众号数据并提供 AI 推荐功能。

## 项目结构

```
wechat_analysis_agent/
├── backend/             # 后端代码
│   ├── api/             # API 模块
│   ├── app.py           # 应用入口
│   ├── config.py        # 配置文件
│   ├── database.py      # 数据库操作
│   └── requirements.txt # 依赖包
├── data/                # 数据文件
├── frontend/            # 前端代码
├── .env.example         # 环境变量示例
├── .gitignore           # Git 忽略文件
└── README.md            # 项目文档
```

## 安装步骤

### 1. 克隆项目

```bash
git clone <repository-url>
cd wechat_analysis_agent
```

### 2. 配置环境变量

复制 `.env.example` 文件为 `.env` 并填写相应的配置信息：

```bash
cp .env.example .env
# 编辑 .env 文件，填写你的 API 密钥和数据库配置
```

### 3. 安装依赖

```bash
cd backend
pip install -r requirements.txt
```

### 4. 启动服务

```bash
cd backend
python app.py
```

服务将在 `http://127.0.0.1:5000` 启动。

## API 文档

### 1. 推荐接口

**URL:** `/api/recommendations`

**方法:** POST

**请求体:**
```json
{
  "session_id": "your_session_id",
  "analysis_data": {
    "data": [
      {
        "title": "文章标题",
        "read_count": 1000,
        "like_count": 100,
        "comment_count": 50
      }
    ],
    "analysis_result": "分析结果"
  }
}
```

**响应:**
```json
{
  "success": true,
  "recommendations": [
    "推荐内容 1",
    "推荐内容 2"
  ],
  "session_id": "your_session_id"
}
```

### 2. 会话接口

**URL:** `/api/sessions`

**方法:** POST

**请求体:**
```json
{
  "user_id": "your_user_id"
}
```

**响应:**
```json
{
  "success": true,
  "session_id": "new_session_id",
  "created_at": "2024-01-01T00:00:00"
}
```

## 技术栈

- **后端框架:** Flask
- **数据库:** MySQL
- **AI 服务:** 火山引擎 API
- **依赖管理:** pip

## 注意事项

- 确保在 `.env` 文件中正确配置所有 API 密钥
- 数据库连接信息需要根据实际情况修改
- 服务默认运行在 5000 端口，如需修改请在 `app.py` 中调整

## 许可证

MIT License