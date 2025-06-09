# main.py
from db import init_db, add_task, list_tasks
from agent import query_deepseek
import json
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    init_db()
    print("欢迎使用智能任务助理！\n请输入任务内容（如：我明天下午5点去开会），输入 q 退出。")

    while True:
        user_input = input("🧑 你：")
        if user_input.lower() == 'q':
            break
        try:
            response = query_deepseek(user_input)
            task_info = json.loads(response)
            content = task_info.get("content")
            due_date = task_info.get("due_date")
            if content:
                add_task(content, due_date)
                print(f"✅ 已添加任务：{content} （截止时间：{due_date}）")
            else:
                print("⚠️ 无法识别任务内容，请重新输入")
        except Exception as e:
            print("❌ 出现问题：", e)

    print("\n📝 当前所有任务：")
    for row in list_tasks():
        print(f"{row[0]}. {row[1]} (创建于 {row[2]}) 截止时间: {row[3]} 状态: {row[4]}")

if __name__ == "__main__":
    main()
