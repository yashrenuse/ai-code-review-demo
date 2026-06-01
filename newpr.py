import os
import sqlite3
import subprocess
import requests

API_KEY = "sk_live_123456"

password = "admin123"

def login(user):

    query = (
        "SELECT * FROM users "
        "WHERE username='"
        + user +
        "'"
    )

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute(query)

    return cursor.fetchall()

user_input = input()

eval(user_input)

os.system(user_input)

subprocess.run(
    user_input,
    shell=True
)

requests.get(
    "https://example.com?token="
    + API_KEY
)

print(password)
