from config.database import get_connection
from psycopg2 import Error

def create_user(name, email):
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
            conn.commit()
        except Error as e:
            print(f"Error creating user: {e}")
        finally:
            cursor.close()
            conn.close()

def get_all_users():
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            rows = cursor.fetchall()
            return rows  
        except Error as e:
            print(f"Error fetching users: {e}")
        finally:
            cursor.close()
            conn.close()

def get_user_by_id(user_id):
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id=%s', (user_id,))
            row = cursor.fetchone()
            return row  
        except Error as e:
            print(f"Error fetching user by ID: {e}")
        finally:
            cursor.close()
            conn.close()
    return None

def update_user(user_id, name, email):
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET name=%s, email=%s WHERE id=%s', (name, email, user_id))
            conn.commit()
        except Error as e:
            print(f"Error updating user: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_user(user_id):
    conn = get_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE id=%s', (user_id,))
            conn.commit()
        except Error as e:
            print(f"Error deleting user: {e}")
        finally:
            cursor.close()
            conn.close()
