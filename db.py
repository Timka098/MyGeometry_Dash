import sqlite3, hashlib
from utils import*
import pygame

# захешувати
def hash_user_password(user_password):
    sha256 = hashlib.sha256()
    sha256.update(user_password.encode('utf-8'))
    return sha256.hexdigest()

# створити базу даних
def create_db():
    conn = sqlite3.connect(abspath('data_base.db'))
    cur = conn.cursor()

    conn.execute("PRAGMA foreign_keys=ON")
    

    cur.execute("""CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY,
    user_name TEXT,
    user_password TEXT
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS result(
    id INTEGER PRIMARY KEY,
    coins INT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
    )""")
    
    conn.commit()
    conn.close()



# створити юзера
def create_user(user_name, user_password):
    conn = sqlite3.connect(abspath('data_base.db'))
    cur = conn.cursor()
    hashed_user_password = hash_user_password(user_password)
    new_player = (user_name, hashed_user_password)
    cur.execute("""INSERT INTO user(user_name, user_password) VALUES(?, ?)""", new_player)
    conn.commit()
    conn.close()

# залогінити юзера
def user_login(user_name, user_password, win):
    
    conn = sqlite3.connect(abspath('data_base.db'))
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM user WHERE user_name = ? AND user_password = ?", (user_name, hash_user_password(user_password)))
    user_info = cur.fetchone()
    
    # ми перебираєм юзерів, якщо серед них нема нашого:
    if user_info == None:
        #!user name or password isn't valid
        return False
    
    else:
        #!login is successful
        return user_info[0]
    
    conn.close()

def create_result(user_id, coins):
    conn = sqlite3.connect(abspath('data_base.db'))
    cur = conn.cursor()
    new_result = (user_id, coins)
    cur.execute("""INSERT INTO result(user_id, coins) VALUES(?, ?)""", new_result)
    
    conn.commit()
    conn.close()
def get_top_results():
    conn = sqlite3.connect(abspath('data_base.db'))
    cur = conn.cursor()
    cur.execute("""SELECT * FROM result ORDER BY coins DESC""")
    return cur.fetchmany(5)
    conn.commit()
    conn.close()
def get_user_name(id):
    conn = sqlite3.connect(abspath('data_base.db'))
    cur = conn.cursor()
    cur.execute("""SELECT * FROM user WHERE id = ?""", (id,))
    return cur.fetchone()[1]
    conn.commit()
    conn.close()