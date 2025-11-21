import sqlite3
import hashlib
import socket
import threading
import logging

#LOGGING SETUP
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

#SAMPLE DATABASE SETUP
def setup_db():
    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    #Creates or Updates userdata.db
    cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        role TEXT NOT NULL DEFAULT 'customer'
        )
    """)

    #Adds sample users if none present
    users = [
        ("mike123", "mikepassword", "admin"),
        ("john", "peanutbutter78", "customer"),
        ("paul111", "ILikeRunning", "customer"),
        ("saul222", "saulpassword", "admin"),
    ]

    for username, raw_password, role in users:
        hashed_password = hashlib.sha256(raw_password.encode()).hexdigest()
        cur.execute("INSERT OR IGNORE INTO userdata (username, password, role) VALUES (?, ?, ?)",
            (username, hashed_password, role))

    conn.commit()
    conn.close()

#CALL DATABASE SETUP
setup_db()

#SOCKET SERVER SETUP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()

#HANDLE CLIENT CONNECTION
def handle_connection(c):
    c.send("Do you want to [login] or [signup]?".encode())
    action = c.recv(1024).decode().lower().strip()

    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    if action == "signup":
        c.send("Choose a username:".encode())
        username = c.recv(1024).decode()
        c.send("Choose a password:".encode())
        raw_password = c.recv(1024).decode()
        password = hashlib.sha256(raw_password.encode()).hexdigest()
        role = "customer" #force customer role so only admin account can create a new admin user

        try:
            cur.execute("INSERT INTO userdata (username, password, role) VALUES (?, ?, ?)",
                        (username, password, role))
            conn.commit()
            c.send("Signup successful! Please log in to continue.".encode())
            logging.info(f"User {username} signed up as a customer.")

            login_user(c, cur)
        except sqlite3.IntegrityError:
            c.send("Username already in use. Please try again.".encode())
            logging.warning(f"Signup failed for {username}. (already exists)")

    elif action == "login":
        login_user(c, cur)

#Handle logins so signup leads automatically to it
def login_user(c, cur):
    c.send("Username:".encode())
    username = c.recv(1024).decode()

    c.send("Password:".encode())
    password = hashlib.sha256(c.recv(1024).decode().encode()).hexdigest()

    cur.execute("SELECT role FROM userdata WHERE username = ? AND password = ?", (username, password))
    row = cur.fetchone()

    if row:
        role = row[0]
        c.send(f"Login Successful! Logged in as {role}.".encode())
        logging.info(f"User '{username}' logged in as {role}.")
    else:
        c.send("Login Failed.".encode())
        logging.warning(f"Failed login attempt: {username}")

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()