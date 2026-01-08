import requests
import sqlite3
from typing import List, Dict

API_URL = "https://openlibrary.org/subjects/data_science.json?limit=5"
DB_NAME = "books.db"


def fetch_books(api_url: str) -> List[Dict]:
    """Fetch book data from external REST API."""
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()
    return response.json().get("works", [])

def initialize_database(db_name: str) -> sqlite3.Connection:
    """Create SQLite database and books table."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            publication_year INTEGER
        )
    """)
    conn.commit()
    return conn


def store_books(conn: sqlite3.Connection, books: List[Dict]) -> None:
    """Insert book records into database."""
    cursor = conn.cursor()
    for book in books:
        title = book.get("title", "NA")
        authors = book.get("authors", [])
        author_names = ", ".join(
            author.get("name", "Unknown") for author in authors
        ) if authors else "Unknown"
        year = book.get("first_publish_year")

        cursor.execute("""
            INSERT INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
        """, (title, author_names, year))
    conn.commit()


def display_books(conn: sqlite3.Connection) -> None:
    """Fetch and display stored books."""
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, publication_year FROM books")
    for row in cursor.fetchall():
        print(row)


def main():
    books = fetch_books(API_URL)
    conn = initialize_database(DB_NAME)
    store_books(conn, books)
    display_books(conn)
    conn.close()


if __name__ == "__main__":
    main()