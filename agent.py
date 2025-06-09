import requests
import json
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
                    "你是一个任务助理，请从用户输入中识别意图（intent）并提取任务信息。" +
                    "返回一个 JSON，格式为：" +
                    "{\"intent\": \"add\"|\"show\"|\"delete\"|\"exit\", \"content\": \"任务内容\", \"due_date\": \"2025-06-15\" 或 null}" +
                    "说明：若用户是要添加任务，请识别为 add，若是查看任务列表为 show，退出为 exit，删除为 delete。" +
                    "若无具体任务内容，content 和 due_date 可设为 null。"
                )
            },
            {"role": "user", "content": prompt}
        ],
        "response_format": {"type": "json_object"}  # 强制返回纯JSON
    }

    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
   
   
    result = response.json()
    # print(result)
    try:
        content_str = result['choices'][0]['message']['content']
        # print(type(content_str))
        # return json.loads(content_str)  
        return content_str
    except (KeyError, json.JSONDecodeError) as e:
        print(f"解析错误: {e}")
        return None
    return result
   