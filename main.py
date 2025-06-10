import sys
import io
import json
from dotenv import load_dotenv

# 设置标准输出为 utf-8，适配中文输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 加载环境变量（如 API KEY）
load_dotenv()

# 导入项目模块
from db import init_db, add_task, list_tasks
from agent import query_deepseek


def display_tasks():
    tasks = list_tasks()
    if not tasks:
        print("📭 当前没有任务")
    else:
        print("\n📝 当前所有任务：")
        for row in tasks:
            print(f"{row[0]}. {row[1]} (创建于 {row[2]}) 截止时间: {row[3]} 状态: {row[4]}")

def main():
    init_db()
    print("欢迎使用 🧠 智能任务助理！\n请输入内容，例如：\n"
          "👉 “我明天下午5点去开会”\n👉 “查看任务”\n👉 “退出”")

    while True:
        user_input = input("🧑 你：").strip()
        if not user_input:
            continue  # 忽略空输入

        try:
            response = query_deepseek(user_input)
            task_info = json.loads(response)

            intent = task_info.get("intent")
            content = task_info.get("content")
            due_date = task_info.get("due_date")

            if intent == 'chat':
                print(f"🤖 助手：{content}")
            elif intent == "add":
                if content:
                    add_task(content, due_date)
                    print(f"✅ 已添加任务：{content}（截止时间：{due_date or '未设置'}）")
                else:
                    print("⚠️ 未识别任务内容，请重新输入")
            elif intent == "show":
                display_tasks()
            elif intent == "exit":
                print("👋 感谢使用，再见！")
                break
            else:
                print("🤖 暂不支持的操作，请尝试重新表述")

        except Exception as e:
            print("❌ 系统异常：", e)


if __name__ == "__main__":
    main()
