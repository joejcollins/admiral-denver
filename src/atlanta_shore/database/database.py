"""Database held in memory."""
import sqlite3


class Database:
    """Sqlite database connection and stuff."""

    def __init__(self, db_path="./data/database.db"):
        """Don't have the database in memory."""
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self) -> None:
        """Create the database every time, look mum no migrations."""
        with self.conn:
            self.conn.execute(
                """CREATE TABLE IF NOT EXISTS images (
                    id INTEGER PRIMARY KEY,
                    file_path TEXT,
                    exif_data TEXT,
                    sky_amount REAL,
                    grass_amount REAL
                )"""
            )
