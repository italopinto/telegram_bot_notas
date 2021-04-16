"""
Module to handle the database, made with sqlite3.
Using the standard python library for SQLite3.
"""

import sqlite3


def create_table():
    """
    Creates the table `reminder` in the database, with only one row to store text
    """
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS reminder(message TEXT)')
    conn.commit()
    conn.close()


def insert_table(content):
    """
    Insert the notes into the table, then reuturns `True`
    """
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO reminder (message) VALUES (?)', (content,))
    conn.commit()
    conn.close()
    return True


def show_table():
    """
    Return a list containing the results of a query `SELECT * FROM reminder
    """
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM reminder')
    results = cur.fetchall()
    conn.close()
    return results

def delete_data():
    """
    Delete all the data in the table `reminder`
    """
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM reminder')
    conn.commit()
    conn.close()

def delete_row(row):
    """
    Return `True` after delete the data (a row) sended by the user
    """
    conn = sqlite3.connect('reminders.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM reminder WHERE message = (?)', (row,))
    conn.commit()
    conn.close()
    return True
