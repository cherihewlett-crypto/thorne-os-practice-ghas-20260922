"""Deliberately vulnerable sample for CodeQL. Not production code.

The first version of this file had the sinks but no sources: `user_input` was a bare function
parameter, so CodeQL's taint tracking had nothing to track FROM and reported zero alerts on a
successful run. A sink alone is not a vulnerability; a path from an untrusted source to that sink
is. `sys.argv` supplies the source here.
"""
import os
import sqlite3
import sys


def lookup(conn: sqlite3.Connection, name: str):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = '" + name + "'")  # py/sql-injection
    return cursor.fetchall()


def run(command: str):
    return os.system("echo " + command)  # py/command-line-injection


if __name__ == "__main__":
    untrusted = sys.argv[1]           # the source
    run(untrusted)                    # source -> command sink
    lookup(sqlite3.connect(":memory:"), untrusted)  # source -> SQL sink
