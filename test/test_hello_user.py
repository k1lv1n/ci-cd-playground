import pytest

from src.hello_user import hello_user


def test_hello_ivan():
    assert hello_user("Ivan") == "Hello, Ivan!", 'Ivan has failed'


def test_hello_bob():
    assert hello_user("Bob") == "Hello, Bob!"


def test_wrong_hello():
    with pytest.raises(AssertionError):
        assert hello_user("Alice") == "Hello, NotAlice!"


if __name__ == '__main__':
    test_hello_ivan()
    test_hello_bob()
    test_wrong_hello()
