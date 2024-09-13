import sqlite3
import mysql.connector
from mysql.connector import Error

# Підключення до SQLite бази даних
sqlite_conn = sqlite3.connect('music.db')
sqlite_cursor = sqlite_conn.cursor()


if mysql_cursor:  # Перевіряємо, чи mysql_cursor визначено
    # Витягуємо дані з SQLite
    sqlite_cursor.execute("SELECT title, artist, img_url, download_url, online_url FROM tracks")
    tracks = sqlite_cursor.fetchall()

    # Вставляємо дані у MySQL
    for track in tracks:
        title, artist, img_url, download_url, online_url = track
        sqlite_cursor.execute('''INSERT INTO tracks (title, artist, img_url, download_url, online_url)
                                VALUES (%s, %s, %s, %s, %s)''', (title, artist, img_url, download_url, online_url))

    # Зберігаємо зміни
    mysql_conn.commit()
    print("Дані успішно перенесені у MySQL базу даних.")

# Закриваємо з'єднання
sqlite_conn.close()
if mysql_conn and mysql_conn.is_connected():
    mysql_conn.close()
