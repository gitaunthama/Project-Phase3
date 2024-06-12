import sqlite3

CONN = sqlite3.connect('tasks.db')
CURSOR = CONN.cursor()
