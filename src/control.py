"""Positive control. If CodeQL does not flag THIS, a clean run proves nothing about the sinks."""
import hashlib


def store_password(password: str) -> str:
    # py/weak-sensitive-data-hashing — needs no taint path, only a weak algorithm on a
    # variable whose name marks it sensitive.
    return hashlib.md5(password.encode()).hexdigest()
# d4 practice — touched to exercise the path filter
