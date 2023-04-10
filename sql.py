import sqlite3


class DataBase():

    def __init__(self, db_file):
        ### database connection
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()


    def user_exists(self, user_id):
        ### check if the user is in the database
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        return bool(len(result.fetchall()))


    def get_user_id(self, user_id):
        ### we get the user id in the database by its user_id in the cart
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        return result.fetchone()[0]


    def add_user(self, user_id):
        ### add user to database
        self.cursor.execute("INSERT INTO users (user_id, language) VALUES(?,?)", (user_id, "English",))
        return self.conn.commit()


    def my_balance_add_user(self, user_id):
        ### Creating an entry in the balance database
        self.cursor.execute("INSERT INTO balances (user_id, dollar_balance, token_balance) VALUES(?,?,?)", (user_id, 5, 50,))
        return self.conn.commit()


    def my_balance_check(self, user_id):
        ### Balance check
        result = self.cursor.execute(f"SELECT token_balance FROM balances WHERE user_id = ?", (user_id,))
        return result.fetchone()[0]


    def my_balance_payment(self, user_id):
        ### Payment Process
        result = self.cursor.execute(f"SELECT dollar_balance,token_balance FROM balances WHERE user_id = ?", (user_id,))
        dollar, token = result.fetchmany(2)[0]
        if (dollar - 0.1) > 0 and (token - 1) > 0:
            self.cursor.execute(f"UPDATE balances SET dollar_balance = ?, token_balance = ? WHERE user_id = ?", (dollar - 0.1, token - 1, user_id,))
            self.conn.commit()
            return True
        else:
            return False


    def update_user_language(self, langid, user_id):
        ### Update users language interface
        self.cursor.execute(f"UPDATE users SET language = ? WHERE user_id = ?", (langid, user_id))
        return self.conn.commit()


    def check_user_laguage(self, user_id):
    ### Check users language
        result = self.cursor.execute(f"SELECT language FROM users WHERE user_id = ?", (user_id,))
        return result.fetchone()[0]

    def close(self):
        ### closing the database
        self.conn.close()
