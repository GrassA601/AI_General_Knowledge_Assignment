```markdown
# 🧠 智能任务助理

一个支持中文自然语言输入的本地任务管理系统。通过 DeepSeek 大模型 API 智能识别用户意图（如添加任务、查看任务、退出等），并将任务信息存入本地数据库，进行管理与展示。

## ✨ 功能特色

- 📝 自然语言提取任务内容和截止时间  
- 🤖 自动判断用户意图（添加 / 查看 / 退出）  
- 💾 本地 SQLite 存储任务  
- 📋 支持任务展示，后续可拓展修改、删除、提醒等功能  

## 🗂️ 项目结构

```

task-assistant/
├── agent.py           # 调用 DeepSeek API 提取任务信息
├── db.py              # SQLite 数据库操作模块
├── main.py            # 主程序：与用户交互，调用智能体和数据库
├── config.py          # 配置文件：DeepSeek API KEY 和 URL
├── requirements.txt   # 项目依赖
├── tasks.db           # 本地数据库（程序运行后生成）
└── README.md          # 项目说明文件

````

## 🧩 使用方式

1. 安装依赖参考  
   ```bash
   pip install -r requirements.txt
````

2. 配置 API Key

   在 `config.py` 中填写你的 API Key 和 URL：

   ```python
   DEEPSEEK_API_KEY = "你的 API Key"
   DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
   ```

3. 运行主程序

   ```bash
   python main.py
   ```

4. 示例输入

   ```
   🧑 你：我下周一上午10点去交论文
   ✅ 已添加任务：交论文（截止时间：2025-06-17）

   🧑 你：查看任务
   📝 当前所有任务：
   1. 交论文 (创建于 2025-06-09) 截止时间: 2025-06-17 状态: 未完成
   ```

5. 退出程序

   表现出关闭意愿即可关闭程序。

## 🛠️ 后续可拓展功能

* ✅ 支持任务状态修改、删除
* 📅 集成日历视图或提醒功能
* 🗣️ 支持语音识别输入
* 🧠 本地模型微调替代 API

## 🙌 鸣谢

* [DeepSeek](https://deepseek.com/) - 提供智能文本理解 API
* 感谢所有 AI 与自动化的探索者

```

```
