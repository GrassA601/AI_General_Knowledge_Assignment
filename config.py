# config.py

import os
from dotenv import load_dotenv

# 自动加载 .env 文件中的环境变量
load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = os.getenv("DEEPSEEK_API_URL")

if not DEEPSEEK_API_KEY or not DEEPSEEK_API_URL:
    raise ValueError("❌ 未正确设置 API 密钥或地址，请在 .env 文件中配置 DEEPSEEK_API_KEY 和 DEEPSEEK_API_URL")
