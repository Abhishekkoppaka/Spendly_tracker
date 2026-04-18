import sqlite3
from datetime import datetime, timedelta
import random
from werkzeug.security import generate_password_hash


def get_db():
    """Returns a SQLite connection to expense_tracker.db with row_factory and foreign keys enabled."""
    conn = sqlite3.connect("expense_tracker.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Creates users and expenses tables using CREATE TABLE IF NOT EXISTS."""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def seed_db():
    """Inserts demo user and 8 sample expenses if users table is empty."""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return

    cursor.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@spendly.com", generate_password_hash("demo123"))
    )
    user_id = cursor.lastrowid

    categories = ["Food", "Transport", "Bills", "Health", "Entertainment", "Shopping", "Other"]
    base_date = datetime(2026, 4, 1)

    sample_expenses = [
        (89.50, "Food", (base_date + timedelta(days=2)).strftime("%Y-%m-%d"), "Grocery shopping at Whole Foods"),
        (15.00, "Transport", (base_date + timedelta(days=5)).strftime("%Y-%m-%d"), "Uber to campus"),
        (120.00, "Bills", (base_date + timedelta(days=7)).strftime("%Y-%m-%d"), "Monthly electricity bill"),
        (45.00, "Health", (base_date + timedelta(days=10)).strftime("%Y-%m-%d"), "Pharmacy prescription"),
        (32.99, "Entertainment", (base_date + timedelta(days=12)).strftime("%Y-%m-%d"), "Netflix and Spotify subscriptions"),
        (156.00, "Shopping", (base_date + timedelta(days=15)).strftime("%Y-%m-%d"), "New running shoes"),
        (28.50, "Food", (base_date + timedelta(days=18)).strftime("%Y-%m-%d"), "Coffee and snacks"),
        (22.00, "Other", (base_date + timedelta(days=21)).strftime("%Y-%m-%d"), "Parking permit renewal"),
    ]

    for amount, category, date, description in sample_expenses:
        cursor.execute(
            "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            (user_id, amount, category, date, description)
        )

    conn.commit()
    conn.close()
