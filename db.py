import sqlite3
from datetime import datetime

DB_PATH = "tasks.db"


def reset_task_ids():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    # 读取所有还存在的任务
    c.execute("SELECT content, due_date, status, created_at FROM tasks ORDER BY id")
    tasks = c.fetchall()

    # 清空表并重建（删除表并重建会使ID重置）
    c.execute("DROP TABLE IF EXISTS tasks")
    c.execute('''
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            due_date TEXT,
            status TEXT DEFAULT 'pending',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 重新插入任务（顺序不变，ID从1开始）
    c.executemany("INSERT INTO tasks (content, due_date, status, created_at) VALUES (?, ?, ?, ?)", tasks)

    conn.commit()
    conn.close()


def get_all_tasks_text():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, content, due_date FROM tasks ORDER BY id")
    rows = c.fetchall()
    conn.close()

    if not rows:
        return "当前没有任务。
    lines = []
    for r in rows:
        due = r[2] if r[2] else "无"
        lines.append(f"{r[0]}. {r[1]} 截止时间: {due}")
    return "\n".join(lines)



def get_tasks_by_ids(ids):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    if not ids:  # ids为空列表或None，直接返回空
        conn.close()
        return []
    
    if ids == "all":  # 约定特殊值 "all" 表示全删
        c.execute("SELECT id, content, due_date FROM tasks")
    else:
        placeholder = ",".join("?" for _ in ids)
        c.execute(f"SELECT id, content, due_date FROM tasks WHERE id IN ({placeholder})", ids)
    
    tasks = c.fetchall()
    conn.close()
    return tasks


def delete_tasks_by_ids_with_confirmation(ids):
    # 先查对应任务
    tasks = get_tasks_by_ids(ids)
    
    if not tasks:
        print("⚠️ 没有找到需要被删除的任务。")
        return
    
    print("以下任务将被删除，请确认：")
    for t in tasks:
        print(f"ID:{t[0]} 内容: {t[1]} 截止: {t[2] or '无'}")
    
    confirm = input("确认删除这些任务吗？(y/n)：").strip().lower()
    if confirm == 'y':
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        if ids == "all":
            c.execute("DELETE FROM tasks")
        else:
            for task_id in ids:
                c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        print("✅ 任务已删除。")
    else:
        print("❌ 已取消删除。")

    
def fetch_all_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, content, due_date FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL,
            due_date TEXT,
            status TEXT DEFAULT 'pending'
        )
    ''')
    conn.commit()
    conn.close()

def add_task(content, due_date=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO tasks (content, created_at, due_date) VALUES (?, ?, ?)
    ''', (content, datetime.now().isoformat(), due_date))
    conn.commit()
    conn.close()

def list_tasks():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    rows = c.fetchall()
    conn.close()
    return rows

def delete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def update_task(task_id, new_content):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('UPDATE tasks SET content = ? WHERE id = ?', (new_content, task_id))
    conn.commit()
    conn.close()
