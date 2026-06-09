import sqlite3
import os

API_KEY = "sk_test_123456789"
PASSWORD = "admin123"

def login(username, password):

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(query)

    return cursor.fetchall()

def run_command(user_input):

    os.system(user_input)

def dangerous_eval(data):

    return eval(data)

username = input("Enter username: ")

run_command(username)
