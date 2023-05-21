import sqlite3, hashlib
from utils import*

# захешувати
def hash_user_password(user_password):
    sha256 = hashlib.sha256()
    sha256.update(user_password.encode('utf-8'))
    return sha256.hexdigest()

# створити базу даних
def create_db():
    conn = sqlite3.connect(abspath('data_base.db'))
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY,
    user_name TEXT,
    user_password TEXT
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
def user_login(user_name, user_password, R, G, B):
    R_old = R

    conn = sqlite3.connect(abspath('data_base.db'))
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM user WHERE user_name = ? AND user_password = ?", (user_name, hash_user_password(user_password)))
    # ми перебираєм юзерів, якщо серед них нема нашого:
    print(R, G, B)
    if cur.fetchone() == None:
        R = 255
        while R > R_old == False:
            R -= 1
            cur.execute("SELECT * FROM user WHERE user_name = ? AND user_password = ?", (user_name, hash_user_password(user_password)))
        print("user name or password isn't valid")
    else: print("login is successful")
    conn.close()


