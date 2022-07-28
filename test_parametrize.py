from dataclasses import dataclass

import pytest


def test_with_param():
    pass


@dataclass
class User:
    id: int
    name: str
    age: int
    description: str


user1 = User(id=1, name="Mario", age=32, description="something " * 10)
user2 = User(id=2, name="Wario", age=62, description="else " * 10)


def test_users(user):
    pass
