.PHONY: help install dev test lint format clean run docker-build docker-run

help:
	@echo "纸飞机 Telegram 机器人 - 可用命令"
	@echo ""
	@echo "开发:"
	@echo "  make install      - 安装依赖"
	@echo "  make dev          - 启动开发服务器"
	@echo "  make run          - 运行机器人"
	@echo ""
	@echo "测试与质量:"
	@echo "  make test         - 运行测试"
	@echo "  make lint         - 代码检查"
	@echo "  make format       - 代码格式化"
	@echo ""
	@echo "其他:"
	@echo "  make clean        - 清理临时文件"
	@echo "  make docker-build - 构建Docker镜像"
	@echo "  make docker-run   - 运行Docker容器"

install:
	pip install -r requirements.txt

dev:
	python main.py

run:
	python main.py

test:
	pytest tests/ -v

lint:
	flake8 . --max-line-length=100 --exclude=venv,__pycache__
	pylint bot/ services/ models/

format:
	black .

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*~" -delete

.db: install
	python scripts/init_db.py

docker-build:
	docker build -t telegram-paper-airplane-bot .

docker-run:
	docker run -d --env-file .env telegram-paper-airplane-bot
