import requests
import json
import re
from config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL

def query_deepseek(prompt):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": (
                    "你是一个智能任务助理，能和用户交流，同时识别用户意图是否为：添加任务(add)、查看任务(show)、删除任务(delete)、退出(exit)。\n"
                    "当用户要添加任务时，提取出任务内容(content)和截止时间(due_date)，"
                    "用 JSON 返回，如：\n"
                    "{\"intent\": \"add\", \"content\": \"交论文\", \"due_date\": \"2025-06-15\"}。\n"
                    "如果无法提取截止时间，请设为 null。\n"
                    "如果用户请求查看任务，返回：{\"intent\": \"show\"}。\n"
                    "退出程序：{\"intent\": \"exit\"}。\n"
                    "如果是闲聊（如“现在几点了”），请自然回答"
                    "返回：{\"intent\": \"chat\", \"content\": content}"
                )
            },
            {"role": "user", "content": prompt}
        ],
        "response_format": {"type": "json_object"}  # 强制返回纯JSON
    }
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
    result = response.json()

    try:
        content_str = result['choices'][0]['message']['content']
        return content_str
    except (KeyError, json.JSONDecodeError) as e:
        print(f"解析错误: {e}")
        return None
    return result
