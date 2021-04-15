import sqlite3


def create_table():
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS reminder(message TEXT)')
    conn.commit()
    conn.close()

def insert_table(content):
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO reminder (message) VALUES (?)', (content,))
    conn.commit()
    conn.close()
    return True

def show_table():
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM reminder')
    results = cur.fetchall()
    conn.close()
    return results

def delete_data():
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM reminder')
    conn.commit()
    conn.close()

def delete_row(row):
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM reminder WHERE message = (?)', (row,))
    conn.commit()
    conn.close()
    return True
