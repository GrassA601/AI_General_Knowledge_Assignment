import sqlite3
from datetime import datetime

DB_PATH = "tasks.db"


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
