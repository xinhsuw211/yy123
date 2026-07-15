# 🛩️ 纸飞机机器人 - Telegram Bot

一个功能完整的 Telegram 纸飞机管理和竞赛机器人，集成了 AI 分析、用户管理、排行榜系统和实时统计功能。

## 📋 功能特性

### 核心功能
- ✈️ **纸飞机管理** - 创建、编辑、删除纸飞机配置
- 🎯 **竞赛管理** - 组织、跟踪和评分竞赛
- 📊 **实时统计** - 飞行数据、距离、精准度统计
- 👥 **用户系统** - 用户注册、等级、成就系统
- 🏆 **排行榜** - 全球、赛季、类别排行榜
- 🤖 **AI 分析** - 飞行分析、建议优化和预测
- 📸 **图像识别** - 使用 OpenCV 检测和追踪纸飞机
- 📈 **数据可视化** - 轨迹图、性能图表
- 💾 **数据持久化** - SQLite + JSON 数据存储
- 🔔 **通知系统** - 竞赛提醒、成就通知

### 高级功能
- 🌍 **多语言支持** - 中文、英文、日文
- 🔐 **权限管理** - 管理员、主持人、玩家角色
- 📅 **赛季系统** - 自动赛季管理和过渡
- 💰 **虚拟货币** - 积分、奖励、商城系统
- 🎮 **成就系统** - 徽章、里程碑、成就解锁
- 📱 **移动端适配** - 完整的内联键盘UI
- 🔄 **自动备份** - 数据自动备份和恢复

## 🚀 快速开始

### 前置要求
- Python 3.8+
- pip (Python 包管理器)
- Telegram Bot Token (从 @BotFather 获取)
- 可选: MongoDB/PostgreSQL (用于生产环境)

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/xinhsuw211/yy123.git
cd yy123
```

2. **创建虚拟环境**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

4. **配置环境变量**
```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 Telegram Bot Token
```

5. **初始化数据库**
```bash
python scripts/init_db.py
```

6. **启动机器人**
```bash
python main.py
```

## 📁 项目结构

```
yy123/
├── main.py                 # 主入口文件
├── requirements.txt        # 项目依赖
├── .env.example           # 环境变量示例
├── config.py              # 配置文件
│
├── bot/
│   ├── __init__.py
│   ├── handlers.py        # 命令处理器
│   ├── filters.py         # 过滤器
│   ├── keyboards.py       # 键盘UI
│   └── utils.py           # 工具函数
│
├── models/
│   ├── __init__.py
│   ├── user.py           # 用户模型
│   ├── airplane.py       # 纸飞机模型
│   ├── competition.py    # 竞赛模型
│   ├── flight.py         # 飞行记录模型
│   └── achievement.py    # 成就模型
│
├── database/
│   ├── __init__.py
│   ├── db.py             # 数据库连接
│   └── queries.py        # 数据库查询
│
├── services/
│   ├── __init__.py
│   ├── user_service.py        # 用户服务
│   ├── airplane_service.py    # 飞机服务
│   ├── competition_service.py # 竞赛服务
│   ├── flight_service.py      # 飞行服务
│   ├── analytics_service.py   # 分析服务
│   ├── ai_service.py          # AI分析服务
│   └── leaderboard_service.py # 排行榜服务
│
├── analyzers/
│   ├── __init__.py
│   ├── image_analyzer.py      # 图像分析
│   ├── flight_analyzer.py     # 飞行分析
│   ├── trajectory_analyzer.py # 轨迹分析
│   └── ai_optimizer.py        # AI优化器
│
├── utils/
│   ├── __init__.py
│   ├── logger.py              # 日志
│   ├── validators.py          # 验证器
│   ├── formatters.py          # 格式化器
│   └── decorators.py          # 装饰器
│
├── data/
│   ├── db.sqlite              # SQLite数据库
│   ├── backups/               # 数据备份
│   └── cache/                 # 缓存文件
│
├── scripts/
│   ├── init_db.py            # 初始化数据库
│   ├── seed_data.py          # 数据填充
│   └── backup.py             # 备份脚本
│
├── tests/
│   ├── __init__.py
│   ├── test_handlers.py      # 处理器测试
│   ├── test_services.py      # 服务测试
│   └── test_analyzers.py     # 分析器测试
│
├── docs/
│   ├── API.md                # API文档
│   ├── COMMANDS.md           # 命令文档
│   ├── DEPLOYMENT.md         # 部署指南
│   └── DEVELOPMENT.md        # 开发指南
│
└── logs/                       # 日志文件
```

## 🎮 使用指南

### 基础命令

```
/start              - 启动机器人
/help               - 显示帮助信息
/me                 - 查看个人资料
/leaderboard        - 查看排行榜
/competitions       - 查看竞赛列表
/my_airplanes       - 查看我的纸飞机
/achievements       - 查看我的成就
/stats              - 查看个人统计
```

### 管理员命令

```
/admin              - 管理员菜单
/create_comp        - 创建竞赛
/end_comp           - 结束竞赛
/ban_user           - 封禁用户
/unban_user         - 解除封禁
/broadcast          - 广播消息
```

### 竞赛命令

```
/join_comp          - 加入竞赛
/leave_comp         - 离开竞赛
/submit_flight      - 提交飞行记录
/comp_leaderboard   - 竞赛排行榜
/comp_info          - 竞赛信息
```

## 🔧 配置说明

### .env 文件配置

```bash
# Telegram Bot
TELEGRAM_BOT_TOKEN=your_bot_token_here

# 数据库
DATABASE_URL=sqlite:///data/db.sqlite
# 或 PostgreSQL
# DATABASE_URL=postgresql://user:password@localhost/dbname

# AI 服务 (可选)
OPENAI_API_KEY=your_openai_key
OPENCV_ENABLED=true

# 日志
LOG_LEVEL=INFO
LOG_FILE=logs/bot.log

# 功能开关
ENABLE_NOTIFICATIONS=true
ENABLE_ANALYTICS=true
ENABLE_AI_ANALYSIS=true

# 管理员
ADMIN_IDS=123456789,987654321
```

## 📊 数据库架构

### 核心表

- **users** - 用户信息
- **airplanes** - 纸飞机配置
- **competitions** - 竞赛信息
- **flights** - 飞行记录
- **achievements** - 成就系统
- **leaderboard** - 排行榜数据
- **transactions** - 虚拟货币交易

## 🤖 AI 功能

### 飞行分析
- 自动检测飞行异常
- 性能指标计算
- 趋势预测

### 优化建议
- 基于历史数据的改进建议
- 对比分析和排名预测
- 个性化训练计划

### 图像识别
- 纸飞机检测
- 轨迹追踪
- 距离测量

## 🧪 测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_handlers.py

# 生成覆盖率报告
pytest --cov=bot --cov=services
```

## 📱 部署

### 本地开发
```bash
python main.py
```

### Docker 部署
```bash
docker build -t telegram-paper-airplane-bot .
docker run -d --env-file .env telegram-paper-airplane-bot
```

### 云平台部署
- Heroku
- AWS Lambda
- Google Cloud Functions
- Azure Functions

详见 [部署指南](docs/DEPLOYMENT.md)

## 🤝 贡献

欢迎提交 Pull Request 和 Issue！

## 📄 许可证

MIT License

## 📞 联系方式

- Telegram: [@PaperAirplaneBotSupport](https://t.me/)
- GitHub Issues: [提交问题](https://github.com/xinhsuw211/yy123/issues)

---

**注意**: 此项目需要正确配置 Telegram Bot Token 才能正常运行。请从 [@BotFather](https://t.me/botfather) 获取您的 Bot Token。
