# ПОЧАТОК РОБОТИ
# Імпорутємо бібліотеку для роботи з sqlite3
import sqlite3
# Створюємо об'єкт, що віповідає за з'єднання з БД та створює БД, якщо її ще нема
conn = sqlite3.connect("players.db")
# Створюємо об'єкт, що віповідає відправку SQL запитів до БД
cur = conn.cursor()
# Створюємо таблицю player, що має 4 поля: id, username, wins, hours_played
cur.execute("""CREATE TABLE IF NOT EXISTS player(
    id INTEGER PRIMARY KEY, 
    user_name TEXT,
    wins INT,
    hours_played INT);
    """)
# Фіксуємо зміни у БД (робимо це завжди після внесення кожної зміни у БД)
#!conn.commit()



# ----------------------------
# СТВОРЕННЯ ЗАПИСІВ У БД

# Додаємо гравця у БД
#! cur.execute("""INSERT INTO player(user_name, wins, hours_played) VALUES("Alex", 12, 20)""")
#! conn.commit()


# Додаємо гравця у БД (зручний спосіб, якщо дані про гравця зберігаються у змінній)
#! new_player = ('Bob', 54668, 46835)
#! cur.execute("""INSERT INTO player(user_name, wins, hours_played) VALUES(?, ?, ?)""", new_player)


# Додаємо одразу багато гравців
#! list_player = [('Hatab', 461, 1000), ('bot1', 0, 1)]
# cur.executemany("""INSERT INTO player(user_name, wins, hours_played) VALUES(?, ?, ?)""", list_player)



# ----------------------------
# ОТРИМАННЯ ДАНИХ З БД
# Отримуємо усі дані з таблиці player
#cur.execute("SELECT * FROM player")
# !fetchall - поверне усі записи з БД
# !print(cur.fetchall())
# fetchone - поверне один  запис з бд
# print(cur.fetchone())
# fetchmany - поверне вказану кількість записів з бд
# print(cur.fetchmany(2))

# отримуємо гравця/гравців, що має/мають к-ть зіграних годин X або білшье 

#! cur.execute("SELECT * FROM player WHERE hours_played >= 1000")
#! print(cur.fetchall())



# ----------------------------
# ВИДАЛЕННЯ ДАНИХ З БД
# Видаляємо гравця/гравців за іменем
#! cur.execute("DELETE FROM player WHERE user_name='bot1'")





# ----------------------------
# ОНОВЛЕННЯ ДАНИХ У БД
# Оновлюємо к-ть поремог гравця/гравців, в к-ть зіграних годин X або білшье 
#cur.execute("UPDATE player SET wins = ? WHERE hours_played >= ?", (100, 1000))



conn.commit()
