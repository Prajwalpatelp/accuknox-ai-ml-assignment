import csv
import sqlite3

DB_NAME = "users.db"
CSV_FILE = "users.csv"


def initialize_database(db_name: str) -> sqlite3.Connection:
    """Create users table if not exists."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    return conn


def import_csv_to_db(conn: sqlite3.Connection, csv_file: str) -> None:
    """Read CSV file and insert data into database."""
    cursor = conn.cursor()
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT OR IGNORE INTO users (name, email)
                VALUES (?, ?)
            """, (row["name"], row["email"]))
    conn.commit()


def display_users(conn: sqlite3.Connection) -> None:
    """Display inserted user records."""
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM users")
    for row in cursor.fetchall():
        print(row)


def main():
    conn = initialize_database(DB_NAME)
    import_csv_to_db(conn, CSV_FILE)
    display_users(conn)
    conn.close()


if __name__ == "__main__":
    main()
