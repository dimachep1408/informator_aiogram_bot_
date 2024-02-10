import sqlite3

connection = sqlite3.connect("bot's database.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Administrators(id INTEGER PRIMARY KEY,Email TEXT NOT NULL, Nickname TEXT NOT NULL,Password TEXT NOT NULL,Phone_number TEXT NOT NULL)")
