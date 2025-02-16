import sqlite3

conn = sqlite3.connect("game.db")
cursor = conn.cursor()

# 创建玩家状态表
cursor.execute("""
    CREATE TABLE IF NOT EXISTS player (
        id INTEGER PRIMARY KEY,
        gold INTEGER DEFAULT 0,
        hacking_level INTEGER DEFAULT 1
    )
""")
conn.commit()

# 增加金币
def update_gold(amount):
    cursor.execute("UPDATE player SET gold = gold + ?", (amount,))
    conn.commit()

# 获取当前金币
def get_gold():
    cursor.execute("SELECT gold FROM player")
    return cursor.fetchone()[0] or 0
