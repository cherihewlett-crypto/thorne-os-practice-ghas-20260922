"""Deliberately vulnerable sample for CodeQL. Not production code, not imported anywhere."""
import os
import sqlite3


def lookup(conn: sqlite3.Connection, user_input: str):
    # CodeQL py/sql-injection: user input concatenated straight into SQL.
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "'")
    return cursor.fetchall()


def run(command: str):
    # CodeQL py/command-line-injection: unsanitised input reaching a shell.
    return os.system("echo " + command)
